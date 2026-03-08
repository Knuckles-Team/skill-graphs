#  [](https://qdrant.tech/documentation/concepts/points/#points)Points
The points are the central entity that Qdrant operates with. A point is a record consisting of a [vector](https://qdrant.tech/documentation/concepts/vectors/) and an optional [payload](https://qdrant.tech/documentation/concepts/payload/).
It looks like this:
```
// This is a simple point
{
    "id": 129,
    "vector": [0.1, 0.2, 0.3, 0.4],
    "payload": {"color": "red"},
}

```

You can search among the points grouped in one [collection](https://qdrant.tech/documentation/concepts/collections/) based on vector similarity. This procedure is described in more detail in the [search](https://qdrant.tech/documentation/concepts/search/) and [filtering](https://qdrant.tech/documentation/concepts/filtering/) sections.
This section explains how to create and manage vectors.
Any point modification operation is asynchronous and takes place in 2 steps. At the first stage, the operation is written to the Write-ahead-log.
After this moment, the service will not lose the data, even if the machine loses power supply.
