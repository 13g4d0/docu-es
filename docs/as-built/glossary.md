# Glosario

| Término | Significado en esta solución |
|---------|------------------------------|
| **Servicio RAG** | Paquete Python y aplicación FastAPI para RAG por etapas (expansión de consulta → embeddings → Vespa → respuesta LLM). En el código coexisten rutas heredadas del paquete histórico `nyrag`. |
| **Vespa** | Motor de búsqueda híbrido / vectorial (`pyvespa`, perfiles de ranking). |
| **Interfaz web de chat** | UI y hub API de chat autohospedados (fork). Frontend: SvelteKit; backend: FastAPI + SQLAlchemy + Redis opcional. |
| **Pasarela de inferencia** | **Gateway** compatible OpenAI: alias de modelo, enrutado, *fallbacks*; a menudo respaldado por PostgreSQL si `STORE_MODEL_IN_DB` está activo. |
| **Proveedor agregador en la nube** | API que concentra modelos de varios proveedores; suele usarse como **fallback** tras la pasarela. |
| **Runtime local en escritorio** | Proceso en el PC que expone API compatible OpenAI (`/v1`) en un puerto configurable. |
| **Enlace remoto al runtime local** | Funciones del ecosistema del runtime de escritorio para operación remota; a menudo junto a red privada alcanzable. |
| **VPN en malla** | Red privada entre nodos con IPs estables en rango típico `100.64.0.0/10` (p. ej. estación ↔ VPS). |
| **Servicio de agentes** | Imagen de contenedor aparte para integraciones de agente / canales de mensajería; API HTTP opcional además del puerto principal de la app. |
| **`dev-stack.sh`** | Orquestación Bash en el repo del servicio RAG para el ciclo de vida Docker de la interfaz de chat y el control de procesos del servicio RAG. |
| **Alias lógico de modelo** | Nombre de modelo visible para el usuario resuelto por la pasarela (p. ej. `lm-auto`) hacia uno o más despliegues *upstream* más reglas de *fallback*. |
