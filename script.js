document.addEventListener("DOMContentLoaded", function() {
  var adminBtn = document.getElementById("adminBtn");
  var alunoBtn = document.getElementById("alunoBtn");
  var sairBtn = document.getElementById("sairBtn");

  adminBtn.addEventListener("click", function() {
    // Chamar a função de login do administrador
    // Você pode usar AJAX ou outra abordagem para fazer uma requisição ao servidor e chamar a função Python fazer_login_admin()
    // Exemplo: fetch('/fazer_login_admin').then(...);
  });

  alunoBtn.addEventListener("click", function() {
    // Chamar a função de login do aluno
    // Você pode usar AJAX ou outra abordagem para fazer uma requisição ao servidor e chamar a função Python fazer_login_aluno()
    // Exemplo: fetch('/fazer_login_aluno').then(...);
  });

  sairBtn.addEventListener("click", function() {
    // Chamar a função de sair
    // Você pode usar AJAX ou outra abordagem para fazer uma requisição ao servidor e chamar a função Python para sair do programa
    // Exemplo: fetch('/sair').then(...);
  });
});
