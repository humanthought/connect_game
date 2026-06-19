**Connect Game**

- This is a game where the first player to connect n pieces in a row (vertical, horizontal or daigonal) wins.
- Currently this game is played as a two player game.

Try it out on docker or kubernetes (via helm):

See https://hub.docker.com/repository/docker/humanthought/connect_game/tags for tag values

Docker:
```
docker run -it humanthought/connect_game:<tag>
```

kubernetes via helm. 
```
helm install connect-game . --set tag=<tag> -n <namespace>
```





