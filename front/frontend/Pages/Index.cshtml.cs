using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using frontend.Contracts;
using System.ComponentModel.DataAnnotations;

namespace IIS_website.Pages
{

    public record TaskCreateDto
    {
        [Required, MinLength(1)]
        public string description { get; set; } = "";
    }
    public class IndexModel : PageModel
    {
        private readonly IHttpClientFactory _httpFactory;

        public List<TaskReadDto> ItemsList { get; private set; } = new();
        
        [BindProperty]
        public TaskCreateDto ItemCreate { get; set; } = new();
        

        public IndexModel(IHttpClientFactory httpFactory)
        {
            _httpFactory = httpFactory;
        }

        public async Task OnGetAsync()
        {
            var client = _httpFactory.CreateClient("api");
            ItemsList = await client.GetFromJsonAsync<List<TaskReadDto>>("/tasks/list")
                        ?? new List<TaskReadDto>();
        }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid) return Page();
            var client = _httpFactory.CreateClient("api");
            var response = await client.PostAsJsonAsync("/tasks/create", ItemCreate);
            return RedirectToPage();
        }
    }

}
