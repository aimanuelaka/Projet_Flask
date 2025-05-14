$(document).ready(function () {
    var table = $('#tableEtudiants').DataTable({
        ajax: '/api/etudiants',
        columns: [
            { data: 'id' },
            { data: 'nom' },
            { data: 'email' },
            {
                data: null,
                render: function (data) {
                    return `
                        <button class="btn btn-sm btn-warning me-1" onclick="modifier(${data.id}, '${data.nom}', '${data.email}')">Modifier</button>
                        <button class="btn btn-sm btn-danger" onclick="supprimer(${data.id})">Supprimer</button>
                    `;
                }
                
            }
        ]
    });

    $('#formAjout').on('submit', function (e) {
        e.preventDefault();
        const nom = $(this).find('input[name="nom"]').val();
        const email = $(this).find('input[name="email"]').val();
        $.ajax({
            url: '/api/etudiants',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ nom: nom, email: email }),
            success: function () {
                table.ajax.reload();
                $('#formAjout')[0].reset();
            }
        });
    });

    window.modifier = function (id, nom, email) {
        const newNom = prompt("Nouveau nom :", nom);
        const newEmail = prompt("Nouvel email :", email);
        if (newNom && newEmail) {
            $.ajax({
                url: `/api/etudiants/${id}`,
                method: 'PUT',
                contentType: 'application/json',
                data: JSON.stringify({ nom: newNom, email: newEmail }),
                success: function () {
                    table.ajax.reload();
                }
            });
        }
    };

    window.supprimer = function (id) {
        if (confirm("Supprimer cet étudiant ?")) {
            $.ajax({
                url: `/api/etudiants/${id}`,
                method: 'DELETE',
                success: function () {
                    table.ajax.reload();
                }
            });
        }
    };
});
