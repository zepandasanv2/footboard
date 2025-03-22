

echo "Setting up your Python environment..."


if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
else
    echo "✅ Virtual environment already exists."
fi


echo "⚙️ Activating virtual environment..."
source venv/Scripts/activate 2>/dev/null || source venv/bin/activate


echo "📥 Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Environment setup complete!"
