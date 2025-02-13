FROM node:latest AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install -g npm@latest
RUN npm ci
COPY . .
RUN npm run build
RUN npm prune --omit=dev

FROM node:latest
WORKDIR /app
COPY --from=builder /app/build build/
COPY --from=builder /app/node_modules node_modules/
COPY package.json .
EXPOSE 3000
ENV NODE_ENV=production
CMD [ "node", "build" ]