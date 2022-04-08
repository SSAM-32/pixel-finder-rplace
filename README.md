# pixel-finder-rplace
uma forma de verificar os pixels colocados por cada usuário no r/place 2022

Baixe os dados do r/place que foram disponibilizados neste link: https://placedata.reddit.com/data/canvas-history/2022_place_canvas_history.csv.gzip

Este arquivo contêm todos os pixels colocados no canvas com horário e id de quem os colocou, porém, o id disponibilizado não é vinculado a sua conta então precisamos encontrá-lo

Para isso, podemos usar o script **placepixel.py** que recebe uma posição específica e imprime todos os usuários que colocaram algum pixel nessa posição. Com isso, você pode escolher um pixel que sabe que colocou e ele irá mostrar uma lista com todos os usuários que interagiram com a posição informada. Possívelmente o seu usuário estará nesta lista.


O script **placepixel.py** contêm 2 propriedades: <br />
FilePath = o caminho do arquivo csv disponibilizado pelo reddit. <br />
coords = as coordenadas do pixel que colocou <br />

Altere as propriedades no código antes de executar, exemplo de preenchimento: <br />
`FilePath = "/home/ssam/Documents/place/2022_place_canvas_history.csv"`<br />
`coords = "1211,576"` <br />
  
saída:<br />
`['2022-04-02 18:09:32.008 UTC', 'rDDcNfxeNX4LH2RS+7eMYieDRohCGXbHqOszAXO3Z9rKhV84hFVnTEJ7zKVYIwZhp7viI8ZRf+6rgsOozufjUg==', '#00A368', '1211,576']`<br />
`['2022-04-02 23:14:33.745 UTC', 'qOn2MRFXdTQkxNAD4z/Vd/O/3FNAlXI2c75xZOcLVizFh2xQYO8/N0jXRx/X/exjf6XzdprykK8zOLOCwr1CxA==', '#FFD635', '1211,576']`<br />
`['2022-04-02 22:22:37.853 UTC', 'xP9fTs4hOCLyfkkE70qeE/FDQnfSciI1zESNUa0hpeznRiCfKTlWCEJsdtYndLHPCG39ZhafDgVAhSVuB/jamw==', '#FFFFFF', '1211,576']`<br />
`['2022-04-02 22:28:30.697 UTC', 'yJB6tKIwwnvfDqW7yjUclq6d4tnY/hcRUX8B0MUAwypJ6fuOWRoBaWzF8ZWgc6vwYNboNNXRZRYRIi2hhauvvg==', '#00A368', '1211,576']`<br />
`['2022-04-04 23:15:41.719 UTC', '96tCXxpHCxxriwAPH1rHAtjf7nuWy18ncgYbUrtaEbAWxFsOsYflVWY/92GROOLo9s03rW0bsnCy0Gw1moRD0g==', '#FFFFFF', '1211,576']`<br />

Após encontrar um id que seja consistente com a colocação de seu pixel (em horário de colocação e cor), utilize o script **placeGenerateImage.py** para gerar uma imagem que contém apenas os pixels do usuário informado.

Exemplo de preenchimento:<br />
`FilePath = "/home/ssam/Documents/place/2022_place_canvas_history.csv"`<br />
`UserID = "96tCXxpHCxxriwAPH1rHAtjf7nuWy18ncgYbUrtaEbAWxFsOsYflVWY/92GROOLo9s03rW0bsnCy0Gw1moRD0g=="`<br />

Após a execução, será aberta uma imagem contendo apenas os pixels colocados pelo usuário informado.
