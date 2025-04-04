function mostrarPagina(id) {
    const telas = document.querySelectorAll('.tela');
    telas.forEach(tela => tela.classList.remove('ativa'));
    document.getElementById(id).classList.add('ativa');
  }
  
  function executarCodigo(id) {
    const codigo = document.getElementById(id).value;
    const iframe = document.getElementById('resultado' + id.slice(-1));
    const erroMsg = document.getElementById('erro' + id.slice(-1));
    try {
      iframe.srcdoc = codigo;
      erroMsg.textContent = "";
    } catch (e) {
      erroMsg.textContent = "Erro ao executar o código: " + e.message;
    }
  }
  