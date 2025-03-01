const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButton = document.getElementById("eventDelete");
const deleteConfirm = document.getElementById("deleteConfirm");

deleteButton.addEventListener("click", (e) => {
    let eventId = e.target.getAttribute("event_id");
    deleteConfirm.href = `event_delete`;
    deleteModal.show();
});