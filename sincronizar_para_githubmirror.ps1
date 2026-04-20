param()

$ErrorActionPreference = "Stop"

$origem = (Resolve-Path $PSScriptRoot).Path
$pai = Split-Path -Parent $origem
$destino = Join-Path $pai "Githubmirror"
$prazoCongelamento = [datetime]::ParseExact(
    "2026-04-24 23:59",
    "yyyy-MM-dd HH:mm",
    [System.Globalization.CultureInfo]::InvariantCulture
)

if ((Get-Date) -gt $prazoCongelamento) {
    throw "Sincronizacao bloqueada: apos 24/04/2026 23:59 a pasta oficial deve permanecer congelada. Trabalhe apenas em Githubmirror."
}

if (-not (Test-Path $destino)) {
    git clone --no-hardlinks --local "$origem" "$destino" | Out-Host
}

$robocopyArgs = @(
    $origem,
    $destino,
    "/MIR",
    "/FFT",
    "/R:2",
    "/W:1",
    "/XD", ".git",
    "/XD", "__pycache__",
    "/XD", ".pytest_cache",
    "/XD", ".mypy_cache",
    "/XD", ".venv",
    "/XD", "venv",
    "/XF", "*.pyc",
    "/XF", "*.pyo"
)

& robocopy @robocopyArgs | Out-Host

if ($LASTEXITCODE -ge 8) {
    throw "Falha ao sincronizar Github para Githubmirror. Codigo do robocopy: $LASTEXITCODE"
}

Write-Host ""
Write-Host "Espelho sincronizado com sucesso:"
Write-Host "Origem : $origem"
Write-Host "Destino: $destino"
Write-Host ""
Write-Host "Apos 24/04/2026 23:59, pare de sincronizar e use apenas Githubmirror para treino e demonstracao."
