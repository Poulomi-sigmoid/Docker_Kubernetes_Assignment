kubectl delete -f airflow-envvars-configmap.yaml
kubectl delete -f airflow-req-configmap.yaml
kubectl delete -f airflow-scheduler-deployment.yaml
kubectl delete -f airflow-scheduler-permissions.yaml
kubectl delete -f airflow-webserver-deployment.yaml
kubectl delete -f airflow-webserver-service.yaml
kubectl delete -f postgres-deployment.yaml
kubectl delete -f postgres-service.yaml
kubectl delete -f airflow-logs-volume.yaml