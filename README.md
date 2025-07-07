# Conversor hashID

## Descrição do projeto:

Este repositório tem como objetia criar uma interface gráfica integrada com a biblioteca hashID, possibilitando a configuração de alguns parâmetros para converter um hash a partir de um hash_ID ou vice-versa.

<br />

# Desenvolvimento

O programa foi desenvolvido em Python, utilizando as bibliotecas PySimpleGUI e hashid.
>Mais abaixo, é instruido como instalar as depêndencias para executar os programas. 

<br />


# Como instalar:
1- Clone o repositório:
```sh
git https://github.com/Gabrielnunesilva/hash_id.git
```

2- Entre na pasta do repositório que você acabou de clonar:
```sh
cd hash_id
```

3- Instale as dependências dos projeto:
```sh
pip install hashid PySimpleGUI
```

4- Execute o programa:
```sh
hash_id.py
```
<br />

# Como Utilizar

A inteface gráfica é simples e amigável, como informado anteriormente ela tem a função de converter um Hash ou Hash_ID.Ao executar o programa, você verá que alguns campos de parametrização. 
<br />
Os campos são Salt, Alphabet, Min length, que basicamente podem ser definidos respectivamente como  semente/segurança, caracteres e largura 
(são parâmetros obrigatórios para o algoritmo da biblioteca hashID). Além disso, tambem tem o campo Hash/ID que é onde você coloca o valor a ser convertido. 
<br />

Para converter o hash a partir de um hash_id, você deve preencher os campos de parametros:
- Salt: Usar um conjunto de caracteres para definir uma "semente" ou "segurança" definindo um nivel de segurança maior (Campo Opcional);
- Alphabet: Preencha com no minimo 16 caracteres únicos, que serão utilizados no valor convertido;
- Min length: Defina o número minimo de caracteres do Hash que será gerado;
- Hash/ID: Coloque o número do hash_id (ou um número inteiro) para a converte-lo em Hash.
<br />
Após isso, basta manter a opção "Gerar" em Hash, e clicar em "Ok". O Hash gerado aparecerá no campo "Resultado", seguindo os parametros definidos acima.
<br />
Para converter o hash em hash_id (ou um número inteiro), basta alterar a opção "Gerar" em ID, colocar o hash no campo "Hash/ID" e apertar em "OK"
<br />
obs: Sempre que for efetuar uma conversão de um Hash ou ID que você tenha gerado, verifique se preencheu os campos corretamente. Sempre que alterar qualquer um dos parametros, a conversão gerará outro hash
ou ID.

<br />
<br />

>Para saber mais sobre a biblioteca hashID, clique aqui: [hashID](https://pypi.org/project/hashID)






