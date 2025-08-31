using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;

namespace PasswordAnalyzer.ViewModels
{
    public class PasswordViewModel : INotifyPropertyChanged
    {
        private string _password;
        private string _strength;
        private string _breachStatus;
        private string _hash;

        public string Password
        {
            get => _password;
            set
            {
                _password = value;
                OnPropertyChanged();
                AnalyzePassword();
            }
        }

        public string Strength
        {
            get => _strength;
            set
            {
                _strength = value;
                OnPropertyChanged();
            }
        }

        public string BreachStatus
        {
            get => _breachStatus;
            set
            {
                _breachStatus = value;
                OnPropertyChanged();
            }
        }

        public string Hash
        {
            get => _hash;
            set
            {
                _hash = value;
                OnPropertyChanged();
            }
        }

        public ICommand CheckBreachCommand { get; }

        public PasswordViewModel()
        {
            CheckBreachCommand = new RelayCommand(CheckBreach);
        }

        private void AnalyzePassword()
        {
            // Logic to analyze password strength and update Strength property
        }

        private void CheckBreach()
        {
            // Logic to check if the password has been breached and update BreachStatus property
        }

        public event PropertyChangedEventHandler PropertyChanged;

        protected void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}