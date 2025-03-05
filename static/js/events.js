/*jshint esversion: 6 */

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButton = document.getElementById("eventDelete");
const deleteConfirm = document.getElementById("deleteConfirm");

deleteButton.addEventListener("click", (e) => {
    deleteConfirm.href = `event_delete`;
    deleteModal.show();
});