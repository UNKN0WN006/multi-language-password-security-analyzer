using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PasswordAnalyzer.Services
{
    public class ApiService
    {
        private readonly HttpClient _httpClient;

        public ApiService(string apiUrl)
        {
            _httpClient = new HttpClient
            {
                BaseAddress = new Uri(apiUrl)
            };
            _httpClient.DefaultRequestHeaders.Accept.Clear();
            _httpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
        }

        public async Task<PasswordAnalysis> AnalyzePasswordAsync(string password)
        {
            var response = await _httpClient.PostAsJsonAsync("api/analyze", new { Password = password });
            response.EnsureSuccessStatusCode();

            var jsonResponse = await response.Content.ReadAsStringAsync();
            return JsonConvert.DeserializeObject<PasswordAnalysis>(jsonResponse);
        }

        public async Task<bool> CheckBreachAsync(string password)
        {
            var response = await _httpClient.GetAsync($"api/breach/{password}");
            return response.IsSuccessStatusCode;
        }
    }
}