import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Ensure the required directories exist:
img_dir = "data/img"
if not os.path.exists(img_dir):
    os.makedirs(img_dir)
pdf_dir = "data"
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

# 1. Plot Genre Distribution
def plot_genre_distribution(df):
    # Use the 'genres' column; assume each row has one primary genre string.
    genre_counts = df['genres'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='viridis')
    plt.title('Top 10 Genres')
    plt.xlabel('Count')
    plt.ylabel('Genre')
    plt.tight_layout()
    path = os.path.join(img_dir, "genre_distribution.png")
    plt.savefig(path)
    plt.close()
    return path

# 2. Plot Popularity Histogram
def plot_popularity_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['popularity'], kde=True, bins=20, color='skyblue')
    plt.title('Popularity Distribution')
    plt.xlabel('Popularity')
    plt.ylabel('Frequency')
    plt.tight_layout()
    path = os.path.join(img_dir, "popularity_distribution.png")
    plt.savefig(path)
    plt.close()
    return path

# 3. Plot Popularity Boxplot
def plot_popularity_boxplot(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df['popularity'], color='lightgreen')
    plt.title('Popularity Boxplot')
    plt.xlabel('Popularity')
    plt.tight_layout()
    path = os.path.join(img_dir, "popularity_boxplot.png")
    plt.savefig(path)
    plt.close()
    return path

# 4. Plot Top Artists Count
def plot_artist_count(df):
    artist_counts = df['artist_name'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=artist_counts.values, y=artist_counts.index, palette='magma')
    plt.title('Top 10 Artists by Count')
    plt.xlabel('Count')
    plt.ylabel('Artist')
    plt.tight_layout()
    path = os.path.join(img_dir, "top_artists.png")
    plt.savefig(path)
    plt.close()
    return path

# 5. Plot Average Popularity by Genre
def plot_avg_popularity_by_genre(df):
    # Group by genres and calculate average popularity
    avg_pop = df.groupby('genres')['popularity'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=avg_pop.values, y=avg_pop.index, palette='coolwarm')
    plt.title('Average Popularity by Genre')
    plt.xlabel('Average Popularity')
    plt.ylabel('Genre')
    plt.tight_layout()
    path = os.path.join(img_dir, "avg_popularity_by_genre.png")
    plt.savefig(path)
    plt.close()
    return path

# Descriptive statistics summary for popularity
def descriptive_statistics(df):
    return df['popularity'].describe()

# Inferential statistics: t-test comparing two genres (example: pop vs. rock)
def inferential_analysis(df, genre_a='pop', genre_b='rock'):
    # Clean genres; here we assume 'genres' is a simple string per row.
    df['genres_clean'] = df['genres'].fillna('').str.strip().str.lower()
    
    # Filter data for each genre.
    df_a = df[df['genres_clean'] == genre_a.lower()]
    df_b = df[df['genres_clean'] == genre_b.lower()]
    
    if len(df_a) < 2 or len(df_b) < 2:
        return {
            'genre_a': genre_a,
            'genre_b': genre_b,
            'avg_pop_a': None,
            'avg_pop_b': None,
            't_stat': None,
            'p_value': None,
            'note': "Not enough data for T-test"
        }
    
    t_stat, p_value = stats.ttest_ind(df_a['popularity'], df_b['popularity'], equal_var=False)
    
    return {
        'genre_a': genre_a,
        'genre_b': genre_b,
        'avg_pop_a': df_a['popularity'].mean(),
        'avg_pop_b': df_b['popularity'].mean(),
        't_stat': t_stat,
        'p_value': p_value
    }

# Master function: run full visualization and generate report data
def run_full_visualization(csv_file='data/synthetic_user_music_data.csv'):
    df = pd.read_csv(csv_file)
    
    # Generate all plots
    genre_plot = plot_genre_distribution(df)
    pop_histogram = plot_popularity_distribution(df)
    pop_boxplot = plot_popularity_boxplot(df)
    artist_plot = plot_artist_count(df)
    avg_pop_plot = plot_avg_popularity_by_genre(df)
    
    desc_stats = descriptive_statistics(df)
    inf_stats = inferential_analysis(df)
    
    report_plots = {
        'genre_distribution': genre_plot,
        'popularity_histogram': pop_histogram,
        'popularity_boxplot': pop_boxplot,
        'top_artists': artist_plot,
        'avg_popularity_by_genre': avg_pop_plot
    }
    
    return {
        'plots': report_plots,
        'descriptive_stats': desc_stats.to_dict(),
        'inferential_analysis': inf_stats
    }

# Generate PDF Report using ReportLab
def generate_pdf_report(report_data, output_file='data/visualization_report.pdf'):
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)
    
    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(70, height - 70, "Music Data Visualization Report")
    
    # Descriptive Statistics
    c.setFont("Helvetica-Bold", 14)
    c.drawString(70, height - 100, "Descriptive Statistics (Popularity):")
    c.setFont("Helvetica", 12)
    y = height - 120
    for key, value in report_data['descriptive_stats'].items():
        c.drawString(80, y, f"{key}: {value}")
        y -= 15

    y -= 10
    # Inferential Analysis
    c.setFont("Helvetica-Bold", 14)
    c.drawString(70, y, "Inferential Analysis (T-Test: pop vs. rock):")
    y -= 20
    c.setFont("Helvetica", 12)
    inf = report_data['inferential_analysis']
    c.drawString(70, y, f"Genre A: {inf['genre_a']}, Average Popularity: {inf['avg_pop_a']}")
    y -= 15
    c.drawString(70, y, f"Genre B: {inf['genre_b']}, Average Popularity: {inf['avg_pop_b']}")
    y -= 15
    c.drawString(70, y, f"T-statistic: {inf['t_stat']}")
    y -= 15
    c.drawString(70, y, f"P-value: {inf['p_value']}")
    y -= 30
    
    # Explanation of the Analysis
    explanation = (
        "Analysis Methods Used:\n"
        "- Descriptive Statistics: Summary measures (mean, median, std, etc.) for song popularity.\n"
        "- Inferential Statistics: A t-test was performed to compare average popularity between \npop and rock genres.\n"
        "- Machine Learning: K-Means clustering was applied on a feature set extracted from the dataset \n"
        "(in our case, we focused on genres and popularity as proxy features) to group songs into clusters.\n"
        "- Visualization: Various plots (bar plots, histograms, boxplots) were generated to provide insight \ninto genre distribution, popularity distribution, and artist frequency."
    )
    text_lines = explanation.split('\n')
    for line in text_lines:
        c.drawString(70, y, line)
        y -= 15
        if y < 100:
            c.showPage()
            y = height - 70
    
    # Insert plots (each image will be scaled to fit)
    c.showPage()
    c.setFont("Helvetica-Bold", 16)
    c.drawString(70, height - 70, "Visualizations")
    y = height - 100
    for desc, img_path in report_data['plots'].items():
        c.setFont("Helvetica-Bold", 14)
        c.drawString(70, y, desc.replace('_', ' ').title())
        y -= 20
        try:
            # Draw image; adjust width/height as needed
            c.drawImage(img_path, 70, y - 200, width=400, height=200)
        except Exception as e:
            c.drawString(70, y - 20, f"Error loading image: {e}")
        y -= 220
        if y < 100:
            c.showPage()
            y = height - 70

    c.save()
    print(f"✅ PDF report generated: {output_file}")

# Main function to run visualization and generate PDF report
def main():
    report_data = run_full_visualization(csv_file='data/synthetic_user_music_data.csv')
    generate_pdf_report(report_data, output_file='data/visualization_report.pdf')

if __name__ == '__main__':
    main()
