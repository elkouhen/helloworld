# AGENTS.md — helloworld

## Rôle du dépôt

`helloworld` est l'application de référence du POC. Elle démontre le contrat
applicatif attendu par la plateforme : monorepo multi-services, CI incluse
depuis `ci-templates`, déploiement GitOps vers `helloworld-iac`.

## Structure

```
helloworld-svc/   API Rust (Axum/Tokio) — port 8000, routes /, /hello/:name, /health
helloworld-gui/   Frontend statique nginx — port 80, proxy /api/ → helloworld-svc
docker-compose.yml  Lancement local (gui:8080, svc:8081)
.gitlab-ci.yml      Généré par le seed plateforme — inclut ci-templates
.releaserc.json     Configuration semantic-release
```

## Développement local

```bash
docker compose up --build
# GUI  → http://localhost:8080
# API  → http://localhost:8081
```

## Contrat avec la plateforme

- Chaque service doit conserver un sous-dossier portant **exactement son nom**
  et un `Dockerfile` à sa racine (Kaniko utilise ce chemin).
- La variable `SERVICES` dans `.gitlab-ci.yml` liste les couples
  `<service>=<image>` séparés par des espaces.
- `SERVICE_NAME` désigne le service vitrine pour les URLs d'environnement GitLab.

## `.gitlab-ci.yml` — fichier géré

Ce fichier est **généré et mis à jour automatiquement** par `gitlab-seed.py`
lors du seed plateforme. Les modifications manuelles peuvent être écrasées à
la prochaine exécution du seed. Pour changer les variables CI, modifier
l'inventaire dans `platform-gitops/argocd/apps/helloworld.yaml`.

## `.releaserc.json` — URL in-cluster

`repositoryUrl` et `gitlabUrl` pointent vers l'URL in-cluster GitLab
(`gitlab-webservice-default.gitlab.svc.cluster.local:8181`). Ces URLs ne sont
pas accessibles depuis une machine locale — `semantic-release` ne peut être
exécuté qu'depuis un runner Kubernetes.

## Ce qu'il ne faut pas faire

- Ne pas déployer directement vers Kubernetes depuis ce dépôt.
- Ne pas modifier les tags d'images dans `helloworld-iac` manuellement — c'est
  le rôle de `deploy.py` dans la CI.
- Ne pas versionner les fichiers `certs/*.crt` produits localement.
