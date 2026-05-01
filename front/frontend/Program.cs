using frontend;
using Prometheus;
using Serilog;
using Serilog.Templates;
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Host.UseSerilog((context, configuration) =>
{
    configuration
        // 1. Najpierw czytamy poziomy logowania (Information, Warning itp.) z appsettings.json
        .ReadFrom.Configuration(context.Configuration)
        
        // 2. Potem w kodzie konfigurujemy konsolę i nasz wymarzony szablon
        .WriteTo.Console(new ExpressionTemplate(
            "{ { '@timestamp': @t, log_level: @l, message: @m, exception: @x, RequestId: RequestId } }\n"
        ));
});

builder.Services.AddHttpClient("api", client =>
{
    client.BaseAddress = new Uri(builder.Configuration["ApiBaseUrl"]);
});
  
var app = builder.Build();

app.UseSerilogRequestLogging();

app.UseHttpMetrics();

app.MapMetrics();

app.UseExceptionHandler("/Error");

app.UseHsts();

app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
