from fastapi import FastAPI
import socket
import datetime

app = FastAPI(
    title="API con Versionado y Tags - Actividad 15",
    description="API desarrollada para demostrar versionado con Git Tags y Docker",
    version="2.0.0"
)

@app.get("/")
def read_root():
    return {
        "mensaje": "Bienvenido a la API Versionada (Versión 2.0.0 - Actualizada)",
        "version": "2.0.0",
        "hostname_contenedor": socket.gethostname(),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/version")
def get_version():
    return {
        "version": "2.0.0",
        "release": "v2.0.0",
        "servicio": "api-versionada-act15",
        "mejoras": [
            "Versionado semántico v2",
            "Etiquetas dinámicas en GHCR",
            "Endpoints optimizados"
        ]
    }

@app.get("/status")
def get_status():
    return {
        "status": "activo",
        "estado": "operativo v2",
        "version": "2.0.0",
        "hostname": socket.gethostname()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
