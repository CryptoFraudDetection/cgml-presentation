from manim import *
from manim_slides import Slide


class Presentation(Slide):
    def construct(self):
        # Title Slide: Show main presentation title with author
        title = VGroup(
            Text("Fraud Detection of Cryptocurrencies", t2c={"[0:15]": BLUE}),
            Text("using Reddit data", t2c={"Reddit": RED}),
            Text(
                "by Gabriel Torres Gamez",
                color=GREY,
            ).scale(0.5),
        ).arrange(DOWN)

        self.play(FadeIn(title))
        self.next_slide()
        self.play(FadeOut(title))

        # Introduction Slide: Present FTC statistics about cryptocurrency fraud
        self.next_slide()

        introduction = VGroup(
            Text("According to a recent analysis"),
            Text("by the Federal Trade Commission,", t2c={"Federal Trade Commission": BLUE}),
            Text("consumers lost over", t2c={"lost": BLUE}),
            Text("$1 billion", color=RED).scale(2),
            Text("to cryptocurrency-related fraud", t2c={"cryptocurrency": BLUE, "fraud": BLUE}),
            Text("between January 2021 and March 2022.", t2c={"January 2021": BLUE, "March 2022": BLUE}),
            Text(
                "«New Analysis Finds Consumers Reported Losing More than $1 Billion in Cryptocurrency to Scams since 2021»,",
                color=GREY,
            ).scale(0.4),
            Text("(2022, Juni 3). Federal Trade Commission.", color=GREY).scale(0.4),
        ).arrange(DOWN)

        self.play(Write(introduction))
        self.next_slide()
        self.play(FadeOut(introduction))

        # Pump and Dump Scheme Visualization: Create animated price chart
        self.next_slide()

        title = Text("Pump and Dump Scheme").scale(1.5)
        self.play(Write(title))
        self.play(FadeOut(title))

        # Set up coordinate system for price chart
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            axis_config={"color": WHITE},
        )
        axes_labels = axes.get_axis_labels(x_label="t", y_label=r"\$")

        # Create pump and dump price function with noise
        def noisy_pump_and_dump(x):
            # Simulate price pump until x=5, then dump
            base = 5 + 90 * np.exp(-((x - 5) ** 2) / 2) if x < 5 else max(0, 100 - 70 * (x - 5))
            # Add random noise for realism
            noise = 2 * np.sin(3 * x) + 2 * np.random.uniform(-1, 1)
            return max(0, base + noise)

        price_graph = axes.plot(
            noisy_pump_and_dump,
            x_range=[0, 9.5],
            color=RED,
            use_smoothing=True,
        )

        # Add labels for key phases of pump and dump
        insider_pump_label = Text("Insiders Pump").next_to(axes.c2p(0.7, 30)).scale(0.5)
        others_pump_label = Text("Others Pump").next_to(axes.c2p(1.7, 70)).scale(0.5)
        dump_label = Text("Dump").next_to(axes.c2p(4.75, 90)).scale(0.5)

        # Animate the price chart elements
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(price_graph))
        self.play(
            Write(insider_pump_label),
            Write(others_pump_label),
            Write(dump_label),
        )

        self.next_slide()
        self.play(
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(price_graph),
            FadeOut(insider_pump_label),
            FadeOut(others_pump_label),
            FadeOut(dump_label),
        )

        # IDEA SLIDE
        self.next_slide()

        idea_title = Text("Idea").to_edge(UL)
        idea_points = VGroup(
            Text("Models trained on social media data before scam events").scale(0.8),
            Text("Detect fraudulent cryptocurrencies using machine learning").scale(0.8),
            Text("Compare graph-based and traditional models").scale(0.8),
        ).arrange(DOWN, aligned_edge=LEFT, buff=1)

        self.play(Write(idea_title))
        self.play(Write(idea_points))
        self.next_slide()
        self.play(FadeOut(idea_title), FadeOut(idea_points))

        # WHY REDDIT SLIDE
        self.next_slide()

        reddit_title = Text("Why Reddit?").to_edge(UL)
        reddit_points = VGroup(
            Text("Reddit offers hierarchical data ideal for graph-based models").scale(0.8),
            Text("Rich social interactions provide meaningful insights").scale(0.8),
            Text("Google and Twitter lacked reliable or suitable data structures").scale(0.8),
        ).arrange(DOWN, aligned_edge=LEFT, buff=1)

        self.play(Write(reddit_title))
        self.play(Write(reddit_points))
        self.next_slide()
        self.play(FadeOut(reddit_title), FadeOut(reddit_points))

        # Data Scraping Process: Show workflow from Google to Reddit to Elasticsearch
        self.next_slide()

        title = Text("Scraping").to_edge(UL)

        # Search query example
        search_query = (
            Text("FTX Token site:reddit.com/r/CryptoCurrency after:2019-08-01 before:2022-11-07", color=GREY)
            .scale(0.5)
            .shift(UP * 1.5)
        )
        rectangle = SurroundingRectangle(search_query, color=GREY, buff=0.3)

        # Platform logos and labels
        google_logo = ImageMobject("img/google_logo.png").scale(0.55).to_edge(LEFT).shift(DOWN * 0.7).shift(RIGHT * 0.5)
        reddit_logo = ImageMobject("img/reddit_logo.png").scale(0.55).shift(DOWN * 0.7)
        elastic_logo = (
            ImageMobject("img/elasticsearch_logo.png").scale(0.55).to_edge(RIGHT).shift(DOWN * 0.7).shift(LEFT * 0.5)
        )

        google_label = Text("Search for Reddit posts").next_to(google_logo, DOWN).scale(0.4)
        reddit_label = Text("Extracting data using praw").next_to(reddit_logo, DOWN).scale(0.4)
        elastic_label = Text("Store data in Elasticsearch").next_to(elastic_logo, DOWN).scale(0.4)

        # Workflow arrows
        arrow = Arrow(google_logo, reddit_logo).shift(DOWN * 1)
        arrow2 = Arrow(reddit_logo, elastic_logo).shift(DOWN * 1)

        # Animate scraping workflow
        self.play(Write(title))
        self.play(
            Write(search_query, run_time=1),
            Create(rectangle),
            FadeIn(google_logo),
            FadeIn(reddit_logo),
            FadeIn(elastic_logo),
            Write(google_label, run_time=1),
            Write(reddit_label, run_time=1),
            Write(elastic_label, run_time=1),
        )
        self.play(Create(arrow))
        self.play(Create(arrow2))

        self.next_slide()
        self.play(
            FadeOut(title),
            FadeOut(search_query),
            FadeOut(rectangle),
            FadeOut(google_logo),
            FadeOut(reddit_logo),
            FadeOut(elastic_logo),
            FadeOut(google_label),
            FadeOut(reddit_label),
            FadeOut(elastic_label),
            FadeOut(arrow),
            FadeOut(arrow2),
        )

        # Data Structure: Show Reddit data schema
        self.next_slide()

        title = Text("Data").to_edge(UL)
        reddit_structure = ImageMobject("img/reddit_structure.png").scale(0.8)
        reddit_structure.set_resampling_algorithm(RESAMPLING_ALGORITHMS["lanczos"])

        self.play(Write(title))
        self.play(FadeIn(reddit_structure))

        self.next_slide()
        self.play(FadeOut(title), FadeOut(reddit_structure))

        # Train-Test Split: Display cryptocurrency dataset division

        self.next_slide()

        coin_image_size = 0.25
        coin_name_size = 0.4
        group_title_size = 0.5

        ts_title = Text("Train - Test split").scale(0.9).to_edge(UL)
        self.play(Write(ts_title))

        # Create train set non-scam coins
        train_non_scam_items = Group(
            *[
                Group(
                    ImageMobject("img/coin.png").scale(coin_image_size),
                    Text(name).scale(coin_name_size),
                ).arrange(DOWN, buff=0.1)
                for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain"]
            ],
        ).arrange(RIGHT, buff=0.5)

        # Create train set scam coins
        train_scam_items = Group(
            *[
                Group(
                    ImageMobject("img/coin.png").scale(coin_image_size),
                    Text(name).scale(coin_name_size),
                ).arrange(DOWN, buff=0.1)
                for name in ["BeerCoin", "BitForex", "Terra Luna"]
            ],
        ).arrange(RIGHT, buff=0.5)

        # Create test set non-scam coins
        test_non_scam_items = Group(
            *[
                Group(
                    ImageMobject("img/coin.png").scale(coin_image_size),
                    Text(name).scale(coin_name_size),
                ).arrange(DOWN, buff=0.1)
                for name in ["Cosmos", "Ethereum"]
            ],
        ).arrange(RIGHT, buff=0.5)

        # Create test set scam coins
        test_scam_items = Group(
            *[
                Group(
                    ImageMobject("img/coin.png").scale(coin_image_size),
                    Text(name).scale(coin_name_size),
                ).arrange(DOWN, buff=0.1)
                for name in ["Safe Moon", "FTX Token"]
            ],
        ).arrange(RIGHT, buff=0.5)

        # Group coins by category
        train_non_scam_group = Group(
            Text("Train Non-Scam").scale(group_title_size),
            train_non_scam_items,
        ).arrange(DOWN, buff=0.3)

        train_scam_group = Group(
            Text("Train Scam").scale(group_title_size),
            train_scam_items,
        ).arrange(DOWN, buff=0.3)

        test_non_scam_group = Group(
            Text("Test Non-Scam").scale(group_title_size),
            test_non_scam_items,
        ).arrange(DOWN, buff=0.3)

        test_scam_group = Group(
            Text("Test Scam").scale(group_title_size),
            test_scam_items,
        ).arrange(DOWN, buff=0.3)

        # Arrange groups for display
        train_set_group = Group(train_non_scam_group, train_scam_group).arrange(DOWN, buff=1)
        test_set_group = Group(test_non_scam_group, test_scam_group).arrange(DOWN, buff=1)
        main_group = Group(train_set_group, test_set_group).arrange(RIGHT, buff=1)

        self.play(FadeIn(main_group))

        # Add dataset statistics
        explanation_text = (
            Group(
                Text("Train set (7 coins): 4 Non-scam, 3 Scam").scale(0.5),
                Text("Test set (4 coins): 2 Non-scam, 2 Scam").scale(0.5),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .to_edge(DOWN)
        )
        self.play(FadeIn(explanation_text))

        self.next_slide()
        self.play(
            FadeOut(ts_title),
            FadeOut(main_group),
            FadeOut(explanation_text),
        )

        # Training Methodology: Show cross-validation process
        self.next_slide()

        tm_title = Text("Training Methodology").scale(0.9).to_edge(UL)
        self.play(Write(tm_title))

        # Create coin groups for cross-validation
        coin_image_size = 0.2
        coins = [
            Group(ImageMobject("img/coin.png").scale(coin_image_size), Text(name).scale(0.4)).arrange(DOWN, buff=0.1)
            for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain", "BeerCoin", "BitForex", "Terra Luna"]
        ]

        all_coins_group = Group(*coins).arrange(RIGHT, buff=0.5).shift(UP)

        validation_placeholder = Rectangle(
            width=all_coins_group.get_width(),
            height=all_coins_group.get_height(),
        ).set_opacity(0)

        # Arrange cross-validation groups
        fitting_group = Group(Text("Fitting Set").scale(0.5), all_coins_group).arrange(RIGHT, buff=0.8)
        validation_group = Group(Text("Validation Set").scale(0.5), validation_placeholder).arrange(RIGHT, buff=0.8)
        main_group = Group(fitting_group, validation_group).arrange(DOWN, buff=0.5)

        self.play(FadeIn(main_group))

        # Animate cross-validation process
        for coin in coins:
            self.play(coin.animate.shift(DOWN * 1.5))
            self.wait(0.5)
            self.play(coin.animate.shift(UP * 1.5))

        self.next_slide()
        self.play(FadeOut(main_group), FadeOut(tm_title))

        # Model Descriptions: Present each classification model

        # TODO: Mention evaluation points
        # Multinomial Naive Bayes
        self.next_slide()
        mnb_title = Text("Multinomial Naive Bayes (Baseline)").scale(0.9).set_color(YELLOW).to_edge(UL)
        mnb_points = VGroup(
            Text("Assumes independence between features").scale(0.8),
            Text("Effective for text classification").scale(0.8),
            Text("Requires numerical input").scale(0.8),
        ).arrange(DOWN, aligned_edge=LEFT, buff=1)

        self.play(Write(mnb_title))
        self.play(Write(mnb_points))
        self.next_slide()
        self.play(FadeOut(mnb_title), FadeOut(mnb_points))

        # Results slide

        # Parameters for sizes
        title_size = 1
        header_size = 0.7
        coin_name_size = 0.7
        score_size = 0.7
        title_buff = 0.2
        column_buff = 1
        group_buff = 2

        title = Text("Metrics").scale(title_size).to_corner(UL)

        scores = {
            "Avalanche": 1,
            "Bitcoin": 1,
            "Chainlink": 1,
            "THORChain": 1,
            "BeerCoin": 0.81,
            "BitForex": 0,
            "Terra Luna": 0,
            "Cosmos": 1,
            "Ethereum": 1,
            "Safe Moon": 0,
            "FTX Token": 0,
        }

        # Vertical groups for train set
        train_coin_names = Group(
            Text("Coin", color=GREY).scale(header_size),  # Header
            *[
                Text(name, color=GREEN if name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain"] else RED).scale(
                    coin_name_size,
                )
                for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain", "BeerCoin", "BitForex", "Terra Luna"]
            ],
        ).arrange(DOWN, buff=title_buff)

        train_scores = Group(
            Text("Accuracy", color=GREY).scale(header_size),  # Header
            *[
                Text(
                    f"{scores[name]}",
                    color=GREEN if name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain"] else RED,
                ).scale(score_size)
                for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain", "BeerCoin", "BitForex", "Terra Luna"]
            ],
        ).arrange(DOWN, buff=title_buff)

        # Vertical groups for test set
        test_coin_names = Group(
            Text("Coin", color=GREY).scale(header_size),  # Header
            *[
                Text(name, color=GREEN if name in ["Cosmos", "Ethereum"] else RED).scale(coin_name_size)
                for name in ["Cosmos", "Ethereum", "Safe Moon", "FTX Token"]
            ],
        ).arrange(DOWN, buff=title_buff)

        test_scores = Group(
            Text("Accuracy", color=GREY).scale(header_size),  # Header
            *[
                Text(f"{scores[name]}", color=GREEN if name in ["Cosmos", "Ethereum"] else RED).scale(score_size)
                for name in ["Cosmos", "Ethereum", "Safe Moon", "FTX Token"]
            ],
        ).arrange(DOWN, buff=title_buff)

        # Combine train and test groups
        train_group = Group(
            Text("Train Set").scale(header_size),
            Group(train_coin_names, train_scores).arrange(RIGHT, buff=column_buff),
        ).arrange(DOWN, buff=title_buff)

        test_group = Group(
            Text("Test Set").scale(header_size),
            Group(test_coin_names, test_scores).arrange(RIGHT, buff=column_buff),
        ).arrange(DOWN, buff=title_buff)

        main_group = Group(train_group, test_group).arrange(RIGHT, buff=group_buff)

        self.play(Write(title))
        self.play(FadeIn(main_group))
        self.next_slide()
        self.play(FadeOut(main_group), FadeOut(title))

        # Linear Support Vector Classifier

        # TODO: Mention that we dont use evaluation points anymore
        self.next_slide()
        svc_title = Text("Linear Support Vector Classifier").scale(0.9).set_color(ORANGE).to_edge(UL)
        svc_points = VGroup(
            Text("Maximizes margin between classes").scale(0.8),
            Text("Requires numerical input").scale(0.8),
            Text("Effective for linearly separable data").scale(0.8),
        ).arrange(DOWN, aligned_edge=LEFT, buff=1)

        self.play(Write(svc_title))
        self.play(Write(svc_points))
        self.next_slide()
        self.play(FadeOut(svc_title), FadeOut(svc_points))

        # Results slide

        # Parameters for sizes
        title_size = 1
        header_size = 0.7
        coin_name_size = 0.7
        score_size = 0.7
        title_buff = 0.2
        column_buff = 1
        group_buff = 2

        title = Text("Metrics").scale(title_size).to_corner(UL)

        scores = {
            "Avalanche": 0.528,
            "Bitcoin": 0.545,
            "Chainlink": 0.515,
            "THORChain": 0.507,
            "BeerCoin": 0.595,
            "BitForex": 0.65,
            "Terra Luna": 0.365,
            "Cosmos": 0.5074,
            "Ethereum": 0.649,
            "Safe Moon": 0.395,
            "FTX Token": 0.428,
        }

        # Vertical groups for train set
        train_coin_names = Group(
            Text("Coin", color=GREY).scale(header_size),  # Header
            *[
                Text(name, color=GREEN if name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain"] else RED).scale(
                    coin_name_size,
                )
                for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain", "BeerCoin", "BitForex", "Terra Luna"]
            ],
        ).arrange(DOWN, buff=title_buff)

        train_scores = Group(
            Text("Accuracy", color=GREY).scale(header_size),  # Header
            *[
                Text(
                    f"{scores[name]}",
                    color=GREEN if name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain"] else RED,
                ).scale(score_size)
                for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain", "BeerCoin", "BitForex", "Terra Luna"]
            ],
        ).arrange(DOWN, buff=title_buff)

        # Vertical groups for test set
        test_coin_names = Group(
            Text("Coin", color=GREY).scale(header_size),  # Header
            *[
                Text(name, color=GREEN if name in ["Cosmos", "Ethereum"] else RED).scale(coin_name_size)
                for name in ["Cosmos", "Ethereum", "Safe Moon", "FTX Token"]
            ],
        ).arrange(DOWN, buff=title_buff)

        test_scores = Group(
            Text("Accuracy", color=GREY).scale(header_size),  # Header
            *[
                Text(f"{scores[name]}", color=GREEN if name in ["Cosmos", "Ethereum"] else RED).scale(score_size)
                for name in ["Cosmos", "Ethereum", "Safe Moon", "FTX Token"]
            ],
        ).arrange(DOWN, buff=title_buff)

        # Combine train and test groups
        train_group = Group(
            Text("Train Set").scale(header_size),
            Group(train_coin_names, train_scores).arrange(RIGHT, buff=column_buff),
        ).arrange(DOWN, buff=title_buff)

        test_group = Group(
            Text("Test Set").scale(header_size),
            Group(test_coin_names, test_scores).arrange(RIGHT, buff=column_buff),
        ).arrange(DOWN, buff=title_buff)

        main_group = Group(train_group, test_group).arrange(RIGHT, buff=group_buff)

        self.play(Write(title))
        self.play(FadeIn(main_group))
        self.next_slide()
        self.play(FadeOut(main_group), FadeOut(title))

        # Graph Attention Network
        self.next_slide()
        gat_title = Text("Graph Attention Network (GAT)").scale(0.9).set_color(GREEN).to_edge(UL)
        gat_graphic = ImageMobject("img/GAT.png").scale(0.9).arrange(DOWN)

        self.play(Write(gat_title))
        self.play(FadeIn(gat_graphic))
        self.next_slide()
        self.play(FadeOut(gat_title), FadeOut(gat_graphic))

        # TODO: Show how GAT transforms a graph

        # Results Slide

        # Parameters for sizes
        title_size = 1
        header_size = 0.7
        coin_name_size = 0.7
        score_size = 0.7
        title_buff = 0.2
        column_buff = 1
        group_buff = 2

        title = Text("Metrics").scale(title_size).to_corner(UL)

        scores = {
            "Avalanche": "0.999...",
            "Bitcoin": 0.761,
            "Chainlink": 0.611,
            "THORChain": 0.633,
            "BeerCoin": 0.318,
            "BitForex": 0.482,
            "Terra Luna": 0.355,
        }

        # Vertical groups for train set
        train_coin_names = Group(
            Text("Coin", color=GREY).scale(header_size),  # Header
            *[
                Text(name, color=GREEN if name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain"] else RED).scale(
                    coin_name_size,
                )
                for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain", "BeerCoin", "BitForex", "Terra Luna"]
            ],
        ).arrange(DOWN, buff=title_buff)

        train_scores = Group(
            Text("Accuracy", color=GREY).scale(header_size),  # Header
            *[
                Text(
                    f"{scores[name]}",
                    color=GREEN if name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain"] else RED,
                ).scale(score_size)
                for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain", "BeerCoin", "BitForex", "Terra Luna"]
            ],
        ).arrange(DOWN, buff=title_buff)

        # Combine train and test groups
        train_group = Group(
            Text("Train Set").scale(header_size),
            Group(train_coin_names, train_scores).arrange(RIGHT, buff=column_buff),
        ).arrange(DOWN, buff=title_buff)

        main_group = Group(train_group).arrange(RIGHT, buff=group_buff)

        self.play(Write(title))
        self.play(FadeIn(main_group))
        self.next_slide()
        self.play(FadeOut(main_group), FadeOut(title))

        # TODO: ADD DISCUSSION SLIDE

        # TODO: ADD THANK YOU SLIDE
