## Passo-a-passo para execução do arquivo

Primeiro deve-se baixar e instalar a versão *stable* do docker para windows

- Acessar: https://hub.docker.com/editions/community/docker-ce-desktop-windows/
- Clickar "Get stable"
- Após download, instalar docker
- Executar o docker, pode dar um 'skip' no tutorial

Depois de instalado, deve-se baixar o container que contém o banco de dados:

- Abrir o programa "Windows power shell" 
	* Apertar tecla do windows + r
	* Escrever "powershell" e executar
- Dentro do powershell, escrever e executar:
	* docker pull glescki/pronondb 
	* docker run --detach --publish 3306:3306 --name pronondb glescki/pronondb

Caso funcione, a janela do docker vai mudar, aparecendo escrito 'pronondb' e 'running' em baixo.

Depois, é clicar duas vezes no arquivo 'main.exe', digitar 'root' como login e 'test' como senha