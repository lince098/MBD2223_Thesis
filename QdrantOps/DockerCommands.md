# Deploying Qdrant cluster in local with Docker

```cmd
docker network create qdrant_network
```

``` cmd
docker run --name qdrant1 ^
-e QDRANT__CLUSTER__ENABLED=true  ^
-p 6333:6333 ^
--network qdrant_network ^
-v "C:\PATH\db1:/qdrant/storage" ^
qdrant/qdrant ./qdrant --uri "http://qdrant1:6335"
```

``` cmd
docker run --name qdrant2 ^
-e QDRANT__CLUSTER__ENABLED=true  ^
-p 6334:6333 ^
--network qdrant_network ^
-v "C:\PATH\db2:/qdrant/storage" ^
qdrant/qdrant ./qdrant --bootstrap "http://qdrant1:6335"
```

``` cmd
docker run --name qdrant3 ^
-e QDRANT__CLUSTER__ENABLED=true  ^
-p 6335:6333 ^
--network qdrant_network ^
-v "C:\PATH\db3:/qdrant/storage" ^
qdrant/qdrant ./qdrant --bootstrap "http://qdrant1:6335"
```