# Shelby AgentVault

AgentVault is a lightweight developer tool that stores AI agent outputs
using Shelby decentralized blob storage.

The goal is to create a permanent and verifiable memory layer
for autonomous AI agents.

## Overview

AI agents often generate valuable outputs such as research logs,
analysis results, and decisions. These outputs are usually stored in
centralized databases, which can be modified or lost.

AgentVault solves this by uploading agent outputs to Shelby
decentralized blob storage, making the data immutable,
verifiable, and permanently accessible.

## Architecture

AI Agent
   ↓
AgentVault
   ↓
Shelby Blob Storage
   ↓
Immutable AI Memory

## How it works

1. AI agent generates output
2. The output is saved locally as a file
3. AgentVault uploads the file using the Shelby CLI
4. Shelby stores the data as a decentralized blob
5. The stored data becomes permanent and verifiable

## Example workflow

AI research agent → generates report → AgentVault uploads to Shelby → permanent storage

## Use cases

- AI research logs
- trading bot activity storage
- dataset storage
- autonomous agent memory
- decentralized AI audit trail

## Future improvements

- API for AI agents
- automated blob uploads
- dashboard for stored agent memories

## Installation

1. Install Shelby CLI
2. Clone this repository

git clone https://github.com/TurgayAcar49/shelby-agentvault.git
cd shelby-agentvault

3. Run the example script

python app.py

## Demo

Example agent output stored with Shelby:

agent_output.txt

Upload example:

shelby blob upload agent_output.txt
