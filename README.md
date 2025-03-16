An awesome project to librate software engineers' bitter life in motion contorl world.

# MCCoder: Streamlining Motion Control with LLM-Assisted Code Generation and Rigorous Verification

## Introduction

MCCoder is an LLM-powered system designed to generate motion control code efficiently and safely. By integrating multitask decomposition, hybrid retrieval-augmented generation (RAG), and iterative self-correction, MCCoder enhances code accuracy using a structured workflow and a well-established motion library. It also features a 3D simulator for motion validation and logs full motion trajectories for verification.

MCCoder is publicly available at [GitHub](https://github.com/MCCodeAI/MCCoder).

## Folder

- **MCEval/**: Contains evaluation data programs and results.
- **docs/**: Includes soft-motion source documentation, sample codes, and the MCEVAL dataset (`WMX3API_MCEval_Evaluation_Dataset`).

## Installation

To install dependencies, run:

```sh
pip install -r requirements.txt
```

## Usage

To launch the main program, run:

```sh
chainlit run app_MCEval.py -w
```

chainlit run app_MCEval.py -w

pip install -r requirements.txt
