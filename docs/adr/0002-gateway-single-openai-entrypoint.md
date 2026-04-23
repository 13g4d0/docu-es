# ADR 0002 — Pasarela única compatible OpenAI para modelos de chat

- **Estado:** Aceptado  
- **Fecha:** 2026-04-23  

## Contexto

La interfaz web de chat puede hablar con muchos proveedores directamente, pero operaciones necesita enrutado unificado, *fallback* y secretos que no deben vivir en cada sesión de navegador.

## Decisión

Enrutar el tráfico principal de *chat completions* por una **única pasarela compatible OpenAI** (en el despliegue de referencia, un producto tipo pasarela unificada). La inferencia local (runtime en escritorio) se conecta como *upstream* alcanzable por **red privada en malla**.

## Consecuencias

- **Positivo:** Política centralizada (alias estilo `lm-auto`), *fallback* y rotación de claves.
- **Negativo:** Pieza adicional en la arquitectura; la DB de pasarela debe respaldarse si `STORE_MODEL_IN_DB` está activo.
