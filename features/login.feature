Feature: Login

  Scenario: Login com credenciais válidas
    Given que eu estou na página de login
    When eu insiro um nome de usuário válido e uma senha válida
    Then eu devo ser redirecionado para a página inicial
