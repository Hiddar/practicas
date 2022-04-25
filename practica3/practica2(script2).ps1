[int]$edad= Read-Host "introduce tu edad "
if ($edad -lt 18){
    Write-Host "aun no eres mayor de edad asi que te sera util esta tabla de multiplicar"
    [int]$tabla= Read-Host "introduce la tabla de multiplicar que quieras ver"
    for ($i=1;$i -lt 11;$i++){
        $r= $tabla * $i
        Write-Host $r
        }
    }
