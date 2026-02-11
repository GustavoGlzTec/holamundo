document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const scheduleItems = document.querySelectorAll('.schedule-item');
    const noResultsMsg = document.getElementById('noResults');
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        let visibleCount = 0;
        scheduleItems.forEach(item => {
            // Get data attributes
            const title = item.getAttribute('data-title').toLowerCase();
            const category = item.getAttribute('data-category').toLowerCase();
            const speakers = item.getAttribute('data-speakers').toLowerCase();
            // Check if search term exists in any of the fields
            if (title.includes(searchTerm) ||
                category.includes(searchTerm) ||
                speakers.includes(searchTerm)) {
                item.style.display = 'flex';
                visibleCount++;
            } else {
                item.style.display = 'none';
            }
        });
        // Show/Hide no results message
        if (visibleCount === 0) {
            noResultsMsg.classList.remove('hidden');
        } else {
            noResultsMsg.classList.add('hidden');
        }
    });
});
