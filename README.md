<h1 align="center">GraphFlow</h1>

<p align="center">
  <b>Where traffic flows, and where it stops.</b><br>
  <sub>Road networks · Routing · ML-based congestion prediction</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-active-green" alt="status">
  <img src="https://img.shields.io/badge/python-3.10+-blue" alt="python">
  <img src="https://img.shields.io/badge/license-MIT-brightgreen" alt="license">
</p>

---

## What is GraphFlow?

GraphFlow is not just another shortest-path library. It answers a harder question:

**"What will the road look like in an hour?"**

Classical routing tells you the shortest path **now**. GraphFlow predicts how traffic will change, which edges will jam, and how to reroute **before** you hit congestion.

Built on the intersection of graph algorithms and machine learning.

---

## Features

- **Road network loading** from OpenStreetMap (`RoadGraph.from_osm()`)
- **Classical routing** — Dijkstra, A*, bidirectional search
- **Edge speed prediction** — ML model trained on road features
- **Congestion forecasting** — predict which edges will slow down
- **Dynamic rerouting** — recalculate path when traffic changes
- **Arrival time uncertainty** — not just ETA, but confidence interval
- **Visualization** — network, routes, congestion heatmaps

---

## Tech Stack

- **Python 3.10+**
- **NetworkX / igraph** — graph structures
- **OSMnx** — OpenStreetMap integration
- **NumPy, scikit-learn** — ML models
- **Matplotlib / Plotly** — visualization

---

## Roadmap

- [ ] Core graph and routing algorithms
- [ ] Edge speed prediction (ML)
- [ ] Congestion-aware dynamic rerouting
- [ ] Arrival time uncertainty estimation
- [ ] Route and flow visualization
- [ ] Publication and documentation

---

## Science

GraphFlow sits at the intersection of:

- **Graph theory** — flow networks, min-cut, max-flow
- **Spatial ML** — edge features, node embeddings
- **Time series** — traffic patterns, periodicity
- **Uncertainty quantification** — ETA confidence intervals

This is not just Dijkstra. This is **routing under uncertainty**.

---

## Author

**Emelyanov Ilya**
GitHub: [@nsdmlk](https://github.com/nsdmlk)

---

## License

MIT © Emelyanov Ilya, 2026

---

<p align="center">
  <sub>Roads are graphs. Traffic is data. GraphFlow connects them.</sub>
</p>
