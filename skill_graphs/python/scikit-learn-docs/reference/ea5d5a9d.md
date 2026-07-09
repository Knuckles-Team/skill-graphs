##  2.3.8. HDBSCAN[#](https://scikit-learn.org/stable/modules/clustering.html#hdbscan "Link to this heading")
The [`HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN") algorithm can be seen as an extension of [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN") and [`OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS"). Specifically, [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN") assumes that the clustering criterion (i.e. density requirement) is _globally homogeneous_. In other words, [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN") may struggle to successfully capture clusters with different densities. [`HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN") alleviates this assumption and explores all possible density scales by building an alternative representation of the clustering problem.
Note
This implementation is adapted from the original implementation of HDBSCAN, [[LJ2017]](https://scikit-learn.org/stable/modules/clustering.html#lj2017).
Examples
  * [Demo of HDBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#sphx-glr-auto-examples-cluster-plot-hdbscan-py)


###  2.3.8.1. Mutual Reachability Graph[#](https://scikit-learn.org/stable/modules/clustering.html#mutual-reachability-graph "Link to this heading")
HDBSCAN first defines dc(xp), the _core distance_ of a sample xp, as the distance to its `min_samples` th-nearest neighbor, counting itself. For example, if `min_samples=5` and x∗ is the 5th-nearest neighbor of xp then the core distance is:
dc(xp)=d(xp,x∗).
Next it defines dm(xp,xq), the _mutual reachability distance_ of two points xp,xq, as:
dm(xp,xq)=max{dc(xp),dc(xq),d(xp,xq)}
These two notions allow us to construct the _mutual reachability graph_ Gms defined for a fixed choice of `min_samples` by associating each sample xp with a vertex of the graph, and thus edges between points xp,xq are the mutual reachability distance dm(xp,xq) between them. We may build subsets of this graph, denoted as Gms,ε, by removing any edges with value greater than ε: from the original graph. Any points whose core distance is less than ε: are at this staged marked as noise. The remaining points are then clustered by finding the connected components of this trimmed graph.
Note
Taking the connected components of a trimmed graph Gms,ε is equivalent to running DBSCAN* with `min_samples` and ε. DBSCAN* is a slightly modified version of DBSCAN mentioned in [[CM2013]](https://scikit-learn.org/stable/modules/clustering.html#cm2013).
###  2.3.8.2. Hierarchical Clustering[#](https://scikit-learn.org/stable/modules/clustering.html#id11 "Link to this heading")
HDBSCAN can be seen as an algorithm which performs DBSCAN* clustering across all values of ε. As mentioned prior, this is equivalent to finding the connected components of the mutual reachability graphs for all values of ε. To do this efficiently, HDBSCAN first extracts a minimum spanning tree (MST) from the fully -connected mutual reachability graph, then greedily cuts the edges with highest weight. An outline of the HDBSCAN algorithm is as follows:
  1. Extract the MST of Gms.
  2. Extend the MST by adding a “self edge” for each vertex, with weight equal to the core distance of the underlying sample.
  3. Initialize a single cluster and label for the MST.
  4. Remove the edge with the greatest weight from the MST (ties are removed simultaneously).
  5. Assign cluster labels to the connected components which contain the end points of the now-removed edge. If the component does not have at least one edge it is instead assigned a “null” label marking it as noise.
  6. Repeat 4-5 until there are no more connected components.


HDBSCAN is therefore able to obtain all possible partitions achievable by DBSCAN* for a fixed choice of `min_samples` in a hierarchical fashion. Indeed, this allows HDBSCAN to perform clustering across multiple densities and as such it no longer needs ε to be given as a hyperparameter. Instead it relies solely on the choice of `min_samples`, which tends to be a more robust hyperparameter.
**[![hdbscan_ground_truth](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_005.png)](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)**
**[![hdbscan_results](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_007.png)](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)**
HDBSCAN can be smoothed with an additional hyperparameter `min_cluster_size` which specifies that during the hierarchical clustering, components with fewer than `minimum_cluster_size` many samples are considered noise. In practice, one can set `minimum_cluster_size = min_samples` to couple the parameters and simplify the hyperparameter space.
References
[[CM2013](https://scikit-learn.org/stable/modules/clustering.html#id10)]
Campello, R.J.G.B., Moulavi, D., Sander, J. (2013). Density-Based Clustering Based on Hierarchical Density Estimates. In: Pei, J., Tseng, V.S., Cao, L., Motoda, H., Xu, G. (eds) Advances in Knowledge Discovery and Data Mining. PAKDD 2013. Lecture Notes in Computer Science(), vol 7819. Springer, Berlin, Heidelberg.
[[LJ2017](https://scikit-learn.org/stable/modules/clustering.html#id9)]
L. McInnes and J. Healy, (2017). Accelerated Hierarchical Density Based Clustering. In: IEEE International Conference on Data Mining Workshops (ICDMW), 2017, pp. 33-42.
