const guardrail = (mathFunction) => {
  const queue = [];
  const result = mathFunction();
  try {
  queue.push(result);
  } catch (error){
    queue.push(error.toString());
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
};

export default guardrail;
