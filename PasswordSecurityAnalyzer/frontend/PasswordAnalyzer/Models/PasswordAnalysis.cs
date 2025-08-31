using System;

namespace PasswordAnalyzer.Models
{
    public class PasswordAnalysis
    {
        public string Password { get; set; }
        public int StrengthScore { get; set; }
        public bool IsBreachDetected { get; set; }
        public string[] Suggestions { get; set; }
        public string HashMD5 { get; set; }
        public string HashSHA256 { get; set; }
        public string HashBcrypt { get; set; }

        public PasswordAnalysis(string password, int strengthScore, bool isBreachDetected, string[] suggestions)
        {
            Password = password;
            StrengthScore = strengthScore;
            IsBreachDetected = isBreachDetected;
            Suggestions = suggestions;
            HashMD5 = GenerateMD5Hash(password);
            HashSHA256 = GenerateSHA256Hash(password);
            HashBcrypt = GenerateBcryptHash(password);
        }

        private string GenerateMD5Hash(string input)
        {
            using (var md5 = System.Security.Cryptography.MD5.Create())
            {
                var inputBytes = System.Text.Encoding.UTF8.GetBytes(input);
                var hashBytes = md5.ComputeHash(inputBytes);
                return BitConverter.ToString(hashBytes).Replace("-", "").ToLowerInvariant();
            }
        }

        private string GenerateSHA256Hash(string input)
        {
            using (var sha256 = System.Security.Cryptography.SHA256.Create())
            {
                var inputBytes = System.Text.Encoding.UTF8.GetBytes(input);
                var hashBytes = sha256.ComputeHash(inputBytes);
                return BitConverter.ToString(hashBytes).Replace("-", "").ToLowerInvariant();
            }
        }

        private string GenerateBcryptHash(string input)
        {
            // Placeholder for bcrypt hashing logic
            return "bcrypt_hash_placeholder"; // Replace with actual bcrypt implementation
        }
    }
}