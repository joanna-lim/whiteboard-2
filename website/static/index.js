function deleteNote(drawingId) {
    fetch('/delete-drawing', {
        method:'POST',
        body: JSON.stringify({ drawingId: drawingId })
    }).then((_res)=>{
        window.location.href="/";
    });
}