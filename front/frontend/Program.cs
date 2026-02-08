using frontend;
using Prometheus;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Services.AddHttpClient("api", client =>
{
    client.BaseAddress = new Uri(builder.Configuration["ApiBaseUrl"]);
});

var app = builder.Build();

app.UseHttpMetrics();

app.MapMetrics();

app.UseExceptionHandler("/Error");

app.UseHsts();

app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
