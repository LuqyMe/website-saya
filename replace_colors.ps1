$files = Get-ChildItem -Path . -Include *.html,*.css -Recurse -File
foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    
    $content = $content -replace '#030305', '#2b0f54'
    $content = $content -replace '#07080e', '#38156e'
    $content = $content -replace '#090a10', '#38156e'
    $content = $content -replace 'rgba\(10, 12, 22, 0.85\)', 'rgba(43, 15, 84, 0.85)'
    $content = $content -replace 'rgba\(5, 5, 8, 0.9\)', 'rgba(43, 15, 84, 0.9)'
    $content = $content -replace '#050508', '#1e0a3c'
    $content = $content -replace '#121420', '#441b82'
    $content = $content -replace 'rgba\(3, 4, 8, 0.95\)', 'rgba(20, 7, 40, 0.95)'
    
    $content = $content -replace '#00f0ff', '#ffd460'
    $content = $content -replace 'rgba\(0, 240, 255', 'rgba(255, 212, 96'
    $content = $content -replace 'cyan-400', 'yellow-400'
    
    $content = $content -replace '#ff0077', '#ff6f61'
    $content = $content -replace '#ff0055', '#ff6f61'
    $content = $content -replace 'rgba\(255, 0, 119', 'rgba(255, 111, 97'
    $content = $content -replace 'pink-500', 'orange-500'
    $content = $content -replace 'pink-400', 'orange-400'
    
    $content = $content -replace '#a855f7', '#ab2e91'
    $content = $content -replace 'purple-400', 'fuchsia-600'
    
    [System.IO.File]::WriteAllText($file.FullName, $content)
}
Write-Output "DONE"
