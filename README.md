# Map Coloring Problem: Australia

In this problem, we aim to color a map of Australia such that no two adjacent regions share the same color. This type of problem is a classic CSP where the goal is to assign colors to regions under specific constraints.

## Problem Setup

- **Variables**: The variables in this problem are the seven states and territories of Australia:
  - Western Australia (WA)
  - Northern Territory (NT)
  - South Australia (SA)
  - Queensland (Q)
  - New South Wales (NSW)
  - Victoria (V)
  - Tasmania (T)

- **Domain**: Each region can be colored with one of three colors, typically represented as `{Red, Green, Blue}`.

- **Constraints**: The main constraint is that no two adjacent regions (regions that share a border) can have the same color. The adjacency relations are as follows:
  - WA is adjacent to NT and SA.
  - NT is adjacent to WA, SA, and Q.
  - SA is adjacent to WA, NT, Q, NSW, and V.
  - Q is adjacent to NT, SA, and NSW.
  - NSW is adjacent to Q, SA, and V.
  - V is adjacent to SA and NSW.
  - T has no adjacent regions (it is an island state).

## Algorithm - Backtracking Search

The backtracking search is used to assign colors to each region, one at a time, while checking constraints at every step:

1. **Select Unassigned Variable**: Choose a region that has not been assigned a color yet.

2. **Order Domain Values**: For the selected region, choose a color from the available domain `{Red, Green, Blue}`.

3. **Check Constraints**: E


