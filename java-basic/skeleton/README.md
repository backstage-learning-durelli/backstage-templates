# ${{ values.name }}

Projeto Spring Boot criado com Backstage, incluindo CI/CD e deploy automático via ArgoCD.

[![CI/CD](https://github.com/backstage-learning-durelli/${{ values.name }}/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/backstage-learning-durelli/${{ values.name }}/actions/workflows/ci-cd.yaml)

## 🚀 Tecnologias

- Java 17
- Spring Boot 3.2.0
- Spring Web
- Spring Actuator
- Maven

## 📋 Pré-requisitos

- Java 17 ou superior
- Maven 3.6 ou superior

## 🔧 Como rodar

### Desenvolvimento

```bash
# Compilar o projeto
mvn clean install

# Executar a aplicação
mvn spring-boot:run
```

A aplicação estará disponível em `http://localhost:8080`

## 🌐 Endpoints

### Hello Endpoint
```
GET http://localhost:8080/api/hello
```

Resposta:
```json
{
  "message": "Hello from ${{ values.name }}!"
}
```

### Health Check
```
GET http://localhost:8080/actuator/health
```

## 🧪 Testes

```bash
# Executar testes
mvn test
```

## 🐳 Docker

```bash
# Build da imagem
docker build -t ${{ values.name }}:latest .

# Executar container
docker run -p 8080:8080 ${{ values.name }}:latest
```

## 🔄 CI/CD e Deploy

### Pipeline Automático (GitHub Actions)

Este projeto possui um pipeline de CI/CD configurado que é executado automaticamente:

**Em Pull Requests:**
- Executa testes unitários

**No branch `main`:**
1. ✅ Executa testes
2. ✅ Builda a aplicação com Maven
3. ✅ Cria imagem Docker
4. ✅ Publica no Docker Hub (`${{ values.dockerUsername }}/${{ values.name }}`)
5. ✅ Atualiza manifestos Kubernetes com nova tag
6. ✅ Commit automático da mudança

### Deploy via ArgoCD

O deploy é gerenciado pelo ArgoCD usando GitOps:

- **Application**: `${{ values.name }}`
- **Namespace**: `${{ values.name }}`
- **Sync Policy**: Automático (prune + self-heal)

**Acessar no ArgoCD:**
```bash
# Via CLI
argocd app get ${{ values.name }}
argocd app sync ${{ values.name }}

# Ver logs
kubectl logs -n ${{ values.name }} -l app=${{ values.name }} -f
```

### Estrutura de Deploy

```
manifests/
├── k8s/
│   ├── deployment.yaml  # Deployment com 2 réplicas
│   ├── service.yaml     # ClusterIP na porta 80
│   └── ingress.yaml     # Ingress (opcional)
```

**Verificar recursos no Kubernetes:**
```bash
# Ver todos os recursos
kubectl get all -n ${{ values.name }}

# Acessar a aplicação (port-forward)
kubectl port-forward -n ${{ values.name }} svc/${{ values.name }} 8080:80
curl http://localhost:8080/api/hello

