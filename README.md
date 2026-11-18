# Actividad 15 - Uso de Versiones y Tags en GitHub y Docker

Repositorio correspondiente a la **Actividad 15: Uso de Versiones y Tags en GitHub y Docker**, para la asignatura de **Gestión del Proceso de Desarrollo de Software**.

---

## 📋 Resumen de la Actividad
1. **API con Endpoints de Versión y Estado:** Se incorporaron `/version` y `/status`.
2. **GitHub Actions con Step `Preparar nombre y etiquetas`:** Generación dinámica de tags a partir de `GITHUB_REF_NAME`.
3. **Control de Versiones:** Uso de `git tag v1.0.0` y `git tag v2.0.0`.
4. **Ejecución Simultánea:** Despliegue en Docker de ambas versiones al mismo tiempo en puertos 8000 y 8001.

---

## 🚀 Comandos de Ejecución Simultánea en Docker

```bash
# Descargar ambas versiones de GHCR
docker pull ghcr.io/emmanuelle2001/act15-docker-tags:v1.0.0
docker pull ghcr.io/emmanuelle2001/act15-docker-tags:v2.0.0

# Ejecutar la Versión 1 en el puerto 8000
docker run -d --name api-v1 -p 8000:8000 ghcr.io/emmanuelle2001/act15-docker-tags:v1.0.0

# Ejecutar la Versión 2 en el puerto 8001
docker run -d --name api-v2 -p 8001:8000 ghcr.io/emmanuelle2001/act15-docker-tags:v2.0.0
```

### Comprobación:
- Versión 1.0.0: `http://localhost:8000/version`
- Versión 2.0.0: `http://localhost:8001/version`
