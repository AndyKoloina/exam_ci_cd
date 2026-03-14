const functions = require('@google-cloud/functions-framework');

// S'exécute quand le topic Pub/Sub reçoit un message
functions.cloudEvent('helloPubSub', cloudEvent => {
  // Le message est dans la data du CloudEvent
  const base64name = cloudEvent.data.message.data;

  const name = base64name
    ? Buffer.from(base64name, 'base64').toString()
    : 'World';

  console.log(`Hello, ${name}!`);
});