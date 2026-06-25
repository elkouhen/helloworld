# helloworld

Application exemple du POC, sous forme de monorepo multi-services :

- `helloworld-svc` : API FastAPI
- `helloworld-gui` : frontend statique nginx

La CI est volontairement minimale : `.gitlab-ci.yml` inclut le template partage `root/ci-templates` et declare les variables propres a cette app.
