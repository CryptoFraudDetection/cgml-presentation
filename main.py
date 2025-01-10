from manim import *
from manim_slides import Slide


class Presentation(Slide):
    # TODO: Remove having to press twice per slide
    # TODO: Look if the presentation reaches 15min
    # TODO: Look if I can host with GitHub Pages

    def construct(self):
        # Title Slide: Show main presentation title with author
        title = VGroup(
            Text("Fraud Detection of Cryptocurrencies", t2c={"[0:15]": RED, "Cryptocurrencies": YELLOW}),
            Text("using Reddit data", t2c={"Reddit": ORANGE}),
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

        title = Text("Pump and Dump Scheme")
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
            Text("Train models on pre-scam data").scale(0.8),
            Text("Detect fraud with machine learning").scale(0.8),
            Text("Compare graph and traditional models").scale(0.8),
        ).arrange(DOWN, aligned_edge=LEFT, buff=1)

        self.play(Write(idea_title))
        self.play(Write(idea_points))
        self.next_slide()
        self.play(FadeOut(idea_title), FadeOut(idea_points))

        # WHY REDDIT SLIDE
        self.next_slide()

        reddit_title = Text("Why Reddit?").to_edge(UL)
        reddit_points = VGroup(
            Text("Hierarchical data for graphs").scale(0.8),
            Text("Probably valuable edges").scale(0.8),
            Text("Many discussions").scale(0.8),
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

        ts_title = Text("Train - Test split").to_edge(UL)
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

        tm_title = Text("Training Methodology").to_edge(UL)
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

        # Animate cross-validation process with parallel movement
        for i, coin in enumerate(coins):
            if i > 0:
                # Move the previous coin up as the current coin moves down
                self.play(
                    coins[i - 1].animate.shift(UP * 1.5),
                    coin.animate.shift(DOWN * 1.5),
                )
            else:
                # Move the first coin down without a previous coin
                self.play(coin.animate.shift(DOWN * 1.5))
            self.wait(0.5)

        # After the loop, move the last coin up
        self.play(coins[-1].animate.shift(UP * 1.5))

        self.next_slide()
        self.play(FadeOut(main_group), FadeOut(tm_title))

        # Model Descriptions: Present each classification model

        # Multinomial Naive Bayes
        self.next_slide()
        mnb_title = Text("Multinomial Naive Bayes (Baseline)").to_edge(UL)
        mnb_points = VGroup(
            Text("Used evaluation points", color=YELLOW).scale(0.8),
            Text("Assumes independence between features").scale(0.8),
            Text("Effective for text classification").scale(0.8),
            Text("Requires numerical input").scale(0.8),
        ).arrange(DOWN, aligned_edge=LEFT, buff=2 / 3)

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
        self.next_slide()
        svc_title = Text("Linear Support Vector Classifier").to_edge(UL)
        svc_points = VGroup(
            Text("Stopped using evaluation points", color=YELLOW).scale(0.8),
            Text("Maximizes margin between classes").scale(0.8),
            Text("Requires numerical input").scale(0.8),
            Text("Effective for linearly separable data").scale(0.8),
        ).arrange(DOWN, aligned_edge=LEFT, buff=2 / 3)

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
        gat_title = Text("Graph Attention Network (GAT)").to_edge(UL)
        gat_title.z_index = 1
        gat_graphic = Group(
            ImageMobject("img/GAT_node.png").scale(0.8),
            ImageMobject("img/GAT_tsne.png").scale(1),
        ).arrange(RIGHT)

        gat_graphic_attribution = (
            VGroup(
                Text(
                    "Veličković, P., Cucurull, G., Casanova, A., Romero, A., Liò, P., & Bengio, Y. (2018).",
                    color=GREY,
                ).scale(0.4),
                Text(
                    "Graph Attention Networks (arXiv:1710.10903). arXiv. https://doi.org/10.48550/arXiv.1710.10903",
                    color=GREY,
                ).scale(0.4),
            )
            .arrange(DOWN, buff=0.2)
            .to_edge(DOWN)
        )
        placeholder = Rectangle(width=1, height=0.4).set_opacity(0)
        gat_graphic_group = Group(placeholder, gat_graphic, gat_graphic_attribution).arrange(DOWN, buff=0.35)

        self.play(Write(gat_title))
        self.play(FadeIn(gat_graphic_group))
        self.next_slide()
        self.play(FadeOut(gat_title), FadeOut(gat_graphic_group))

        # Results Slide
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

        # DISCUSSION SLIDE
        self.next_slide()

        discussion_scale = 0.65  # Parameter for scaling text

        # Title
        discussion_title = Text("Discussion").to_edge(UL)

        # Results section
        results_title = Text("Results", color=BLUE).scale(discussion_scale)
        results_points = VGroup(
            Text("1. Models struggled with scams").scale(discussion_scale),
            Text("2. Reddit lacks predictive signals").scale(discussion_scale),
            Text("3. Imbalanced dataset limits accuracy").scale(discussion_scale),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        results_group = VGroup(results_title, results_points).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # Improvements section
        improvements_title = Text("Possible Improvements", color=GREEN).scale(discussion_scale)
        improvements_points = VGroup(
            Text("1. Fine-tune embeddings").scale(discussion_scale),
            Text("2. Use richer graph data").scale(discussion_scale),
            Text("3. Add price and volume data").scale(discussion_scale),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        improvements_group = VGroup(improvements_title, improvements_points).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # Align the two groups side by side
        discussion_content = VGroup(results_group, improvements_group).arrange(RIGHT, buff=1)

        # Animate slide elements
        self.play(Write(discussion_title))
        self.play(Write(discussion_content))
        self.next_slide()
        self.play(FadeOut(discussion_title), FadeOut(discussion_content))

        # THANK YOU SLIDE
        self.next_slide()

        main_text = Text("Thank you for your attention!").scale(1.5)
        self.play(Write(main_text))
