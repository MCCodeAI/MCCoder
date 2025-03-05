from typing import List, Callable, Union, Optional
from collections import defaultdict
import traceback

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAI

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

class AgentX:
    """
    Represents an intelligent agent with specific configurations and states, supporting flexible LLM models.
    """
    def __init__(
        self,
        name: str = "Agent X",
        llm: object = ChatOpenAI(model="gpt-4o-mini"),
        instructions: Union[str, Callable[[], str]] = "You are an intelligent agent. Your name is weiwei",
        functions: Optional[List[Callable]] = None,
        chat_history: Optional[List[Union[HumanMessage, SystemMessage, AIMessage]]] = None,
        working_state: str = "idle",
        output_format: str = "text",
        streaming: bool = True  # Add streaming parameter with default value True
    ):
        """
        Initialize the AgentX with the given parameters.

        :param name: Name of the agent.
        :param llm: The LLM object used by the agent (e.g., OpenAI, Hugging Face, etc.).
        :param instructions: Instructions for the agent. Can be a string or a callable returning a string.
        :param functions: A list of callable functions the agent can use.
        :param chat_history: A list of HumanMessage, SystemMessage, or AIMessage objects representing chat history.
        :param working_state: The current state of the agent (e.g., "idle", "working").
        :param output_format: The desired format of the output (e.g., "text", "json").
        """
        self.name = name
        self.llm = llm
        self.instructions = instructions
        self.functions = functions or []
        self.chat_history = chat_history or [SystemMessage(content=self.instructions)]
        self.working_state = working_state
        self.output_format = output_format
        self.streaming = streaming

    def update_working_state(self, state: str):
        """
        Updates the working state of the agent.

        :param state: The new state of the agent (e.g., "idle", "working").
        """
        self.working_state = state

    def add_to_chat_history(self, message: Union[HumanMessage, SystemMessage, AIMessage]):
        """
        Adds a new message to the chat history.

        :param message: The message to add, which can be a HumanMessage, SystemMessage, or AIMessage.
        """
        self.chat_history.append(message)

    def update_instructions(self, new_instructions: str):
        """
        Updates the agent's instructions and adds the updated instructions to the chat history 
        as a SystemMessage.

        :param new_instructions: The new instructions to update.
        """
        self.instructions = new_instructions
        self.add_to_chat_history(SystemMessage(content=self.instructions))

    def reset_chat_history(self):
        """
        Clears the chat history and resets it with the initial system message.
        """
        self.chat_history = [SystemMessage(content=self.instructions)]

    def set_output_format(self, format: str):
        """
        Updates the output format.

        :param format: The new output format (e.g., "text", "json").
        """
        self.output_format = format

    def execute_function(self, function_name: str, **kwargs) -> Union[str, dict]:
        """
        Executes a function from the functions list by name.

        :param function_name: The name of the function to execute.
        :param kwargs: Arguments to pass to the function.
        :return: The result of the function execution.
        """
        func_map = {f.__name__: f for f in self.functions}
        if function_name in func_map:
            return func_map[function_name](**kwargs)
        raise ValueError(f"Function {function_name} not found in the agent's function list.")

    def stream_response(self, user_prompt: str, **kwargs):
        """
        Generates a response from the LLM using the current chat history with streaming output.

        :param user_prompt: The input prompt to the agent.
        :param kwargs: Additional parameters for the LLM.
        :yield: Yields the response content incrementally.
        """
        try:
            
            # Add the user's prompt to the chat history
            self.add_to_chat_history(HumanMessage(content=user_prompt))

            # Process the streaming response
            partial_response = ""
            for response in self.llm.invoke(self.chat_history, stream=True):
                if response[0] == 'content':
                    partial_response += str(response[1])
                    # Yield each part of the response as it arrives
                    yield str(response[1])
                else:
                    break
            # Add the complete response to the chat history
            
            self.chat_history.pop()# Removes the last message from the chat history. This is typically done to prevent redundant or verbose prompts in the history.

            self.add_to_chat_history(HumanMessage(content=user_prompt.splitlines()[0])) # Adds only the first line of the user prompt as a new message in the chat history. This ensures the agent retains the primary context or intent of the user's input while reducing verbosity and not reaching llm's context limit.

            self.add_to_chat_history(AIMessage(content=partial_response))
            print(self.chat_history)

        except Exception as e:
            # Capture the full traceback
            tb = traceback.format_exc()
            error_message = f"Error in generate_response: {str(e)}\nTraceback:\n{tb}"
            yield error_message

    def generate_response(self, user_prompt: str, **kwargs):
        """
        Generates a complete response from the LLM using the current chat history.

        :param user_prompt: The input prompt to the agent.
        :param kwargs: Additional parameters for the LLM.
        :return: The complete response content as a string.
        """
        try:
            # Add the user's prompt to the chat history
            self.add_to_chat_history(HumanMessage(content=user_prompt))

            # Get the response from the LLM
            response = self.llm.invoke(self.chat_history)

            # Check if the response contains content
            if response and hasattr(response, 'content'):
                complete_response = response.content
            else:
                complete_response = "No response content returned by LLM."

            self.chat_history.pop()# Removes the last message from the chat history. This is typically done to prevent redundant or verbose prompts in the history.

            self.add_to_chat_history(HumanMessage(content=user_prompt.splitlines()[0])) # Adds only the first line of the user prompt as a new message in the chat history. This ensures the agent retains the primary context or intent of the user's input while reducing verbosity and not reaching llm's context limit.

            # Add the complete response to the chat history
            self.add_to_chat_history(AIMessage(content=complete_response))

            # Return the complete response
            return complete_response

        except Exception as e:
            # Capture the full traceback
            tb = traceback.format_exc()
            error_message = f"Error in generate_response: {str(e)}\nTraceback:\n{tb}"
            return error_message