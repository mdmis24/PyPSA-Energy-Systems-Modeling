# PyPSA-Energy-Systems-Modeling
A progressive tutorial series on energy system modeling and sector coupling using PyPSA, from basic market clearing to industrial symbiosis.


# Applied Energy System Modeling with PyPSA

This repository serves as a progressive, tutorial-style portfolio demonstrating the design, optimization, and analysis of energy systems using [PyPSA](https://pypsa.org/) (Python for Power System Analysis). 

The models scale in complexity, beginning with foundational market-clearing mechanisms and culminating in full-scale industrial symbiosis (Sector Coupling) and Power-to-X (PtX) integration. 

## 🎯 Project Scope and Objectives

The primary goal of this repository is to demonstrate practical, reproducible energy system modeling. Rather than relying on theoretical data, these models are grounded in real-world Nordic energy dynamics. 

**Key Data Sources:**
*   **Weather & Generation Profiles:** Authentic meteorological data and capacity factors sourced via Renewables.ninja.
*   **Market Data:** Historical Day-Ahead market clearing prices for the DK1 (Western Denmark) bidding zone.
*   **Technology Parameters:** Cost, efficiency, and lifetime metrics adapted from the Danish Energy Agency (DEA) Technology Data catalogues.

## 🗂️ Repository Roadmap (Table of Contents)

This series is designed to be explored chronologically. 

*   **[01. Basic Generation and Markets](./01-Basic-Generation-and-Markets)** 
    *   *Focus:* Single-node modeling, integrating variable renewable energy (VRE), and clearing against DK1 Day-Ahead prices.
*   **[02. Adding Storage Dynamics](./02-Adding-Storage-Dynamics)** *(Work in Progress)*
    *   *Focus:* Battery Energy Storage Systems (BESS), arbitrage strategies, and inter-temporal constraints.
*   **[03. Thermal Systems and Sector Coupling](./03-Thermal-Systems)** *(Planned)*
    *   *Focus:* Heat pumps, electric boilers, and utilizing waste heat streams.
*   **[04. Industrial Symbiosis & Power-to-X](./04-Industrial-Symbiosis-PtX)** *(Planned)*
    *   *Focus:* Multi-vector energy parks, hydrogen production, and cross-sector resource optimization.

## ⚙️ Setup and Installation

To run these notebooks locally, you will need an optimization solver (such as HiGHS, CBC, or Gurobi) and the required Python packages.

1. Clone this repository:
   ```bash
   git clone [https://github.com/mdmis24/PyPSA-Energy-Systems-Modeling.git](https://github.com/mdmis24/PyPSA-Energy-Systems-Modeling.git)
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
