# OpenAI: Curso 1

## ⚙️ Configuração do Ambiente

### Criando e Ativando o Ambiente Virtual

**Windows:**
```bash
python -m venv curso_1_openai
curso_1_openai\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv curso_1_openai
source curso_1_openai/bin/activate
```

### Instalação das Bibliotecas

```bash
pip install openai python-dotenv tiktoken
```

### Erros de API
Uma visão geral dos erros que podem ocorrer com a API.

**401 - Invalid Authentication**

Causa: a autenticação fornecida é inválida.
Solução: verifique se a chave de API correta e a organização solicitante estão sendo usadas. Certifique-se de que a autenticação esteja configurada corretamente para a chamada da API.
401 - Incorrect API key provided

Causa: a chave de API fornecida não está correta.
Solução: verifique se a chave de API usada está correta. Se houver problemas persistentes, você pode tentar limpar o cache do navegador ou gerar uma nova chave de API válida.
401 - You must be a member of an organization to use the API

Causa: sua conta não faz parte de uma organização.
Solução: entre em contato com a equipe de suporte da OpenAI para te adicionar em uma nova organização. Outra alternativa é pedir a alguém da sua organização para te convidar para fazer parte dela.
429 - Rate limit reached for requests

Causa: você está enviando solicitações com muita rapidez, excedendo o limite da taxa.
Solução: diminua a velocidade das suas solicitações para cumprir os limites de taxa. Consulte o guia de limite de taxa fornecido pela OpenAI (em inglês) para entender as diretrizes.
429 - You exceeded your current quota, please check your plan and billing details

Causa: você atingiu o limite máximo de gastos mensais (limite rígido) definido para sua conta.
Solução: se você deseja aumentar esse limite, pode solicitar um aumento de quota à OpenAI. Verifique também seus detalhes de plano e faturamento.
500 - The server had an error while processing your request

Causa: houve um problema nos servidores da OpenAI ao processar sua solicitação.
Solução: espere por um curto período e tente enviar a solicitação novamente. Se o problema persistir, entre em contato com a equipe de suporte da OpenAI e verifique se há informações adicionais na página de status da OpenAI.
503 - The engine is currently overloaded, please try again later

Causa: os servidores da OpenAI estão enfrentando um alto tráfego e estão sobrecarregados.
Solução: aguarde por um curto período e tente novamente mais tarde. Isso geralmente ocorre quando há um grande volume de solicitações sendo processadas simultaneamente.
Erros do Python
Aqui está uma descrição de cada um dos tipos de erros da biblioteca Python da OpenAI:

### APIError

Causa: ocorreu um problema do lado da OpenAI.
Solução: espere por um curto período e tente enviar a solicitação novamente. Se o problema persistir, entre em contato com a equipe de suporte da OpenAI. Esse erro geralmente indica uma falha interna nos servidores da OpenAI.
Timeout

Causa: a solicitação atingiu o tempo limite.
Solução: espere por um curto período e tente enviar a solicitação novamente. Se o problema persistir, entre em contato com a equipe de suporte da OpenAI. Isso pode ocorrer quando a solicitação leva muito tempo para ser processada.
RateLimitError

Causa: você atingiu o limite de taxa atribuído.
Solução: diminua a velocidade das suas solicitações para cumprir os limites de taxa. Consulte o guia de limite de taxa fornecido pela OpenAI para entender as diretrizes.
APIConnectionError

Causa: houve um problema ao se conectar aos serviços da OpenAI.
Solução: verifique suas configurações de rede, configuração de proxy, certificados SSL ou regras de firewall. Certifique-se de que sua conexão com a Internet esteja funcionando corretamente.
InvalidRequestError

Causa: sua solicitação estava malformada ou faltava alguns parâmetros obrigatórios, como um token ou entrada.
Solução: o erro deve fornecer detalhes sobre o erro específico. Consulte a documentação do método de API específico que você está chamando e verifique se você está enviando parâmetros válidos e completos. Verifique também a codificação, formato ou tamanho dos dados da sua solicitação.
AuthenticationError

Causa: sua chave de API ou token era inválida, expirou ou foi revogada.
Solução: verifique sua chave de API ou token e certifique-se de que ela esteja correta e ativa. Se necessário, gere uma nova chave de API a partir do painel da sua conta.
ServiceUnavailableError

Causa: ocorreu um problema nos servidores da OpenAI.
Solução: espere por um curto período e tente enviar a solicitação novamente. Se o problema persistir, entre em contato com a equipe de suporte da OpenAI e verifique se há informações adicionais na página de status da OpenAI.