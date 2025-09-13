// ===== Funções de usuários =====

// Salvar usuário no LocalStorage
function salvarUsuario(usuario) {
    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];
    usuarios.push(usuario);
    localStorage.setItem("usuarios", JSON.stringify(usuarios));
}

// Buscar usuário pelo login
function buscarUsuario(username, password) {
    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];
    return usuarios.find(u => u.username === username && u.password === password);
}

// ===== Cadastro =====
const cadastroForm = document.getElementById("cadastroForm");
if (cadastroForm) {
    cadastroForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const nome = document.getElementById("nome").value;
        const email = document.getElementById("email").value;
        const telefone = document.getElementById("telefone").value;
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        const usuario = { nome, email, telefone, username, password };

        salvarUsuario(usuario);

        alert("Cadastro realizado com sucesso!");
        window.location.href = "login.html"; // Redireciona para login
    });
}

// ===== Login =====
const loginForm = document.getElementById("loginForm");
if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        const usuario = buscarUsuario(username, password);

        if (usuario) {
            alert(`Bem-vindo, ${usuario.nome}!`);
            // Redireciona para página de aluguel
            window.location.href = "aluguel.html";
        } else {
            alert("Usuário ou senha inválidos.");
        }
    });
}

// ===== Aluguel de EPIs =====
function adicionarAoCarrinho(epi) {
    let carrinho = JSON.parse(localStorage.getItem("carrinho")) || [];
    carrinho.push(epi);
    localStorage.setItem("carrinho", JSON.stringify(carrinho));
    alert(`${epi} adicionado ao carrinho!`);
}

// Captura os botões de "Alugar" na página aluguel.html
const botoesAlugar = document.querySelectorAll(".btn-alugar");
if (botoesAlugar.length > 0) {
    botoesAlugar.forEach(botao => {
        botao.addEventListener("click", () => {
            const epi = botao.getAttribute("data-epi");
            adicionarAoCarrinho(epi);
        });
    });
}
