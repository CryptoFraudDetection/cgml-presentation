from manim import *
from manim_slides import Slide


class Presentation(Slide):
    def construct(self):
        # --- Title Slide ---

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

        # --- Introduction Slide ---

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

        # --- isualization of Pump and Dump Scheme ---

        self.next_slide()

        title = Text("Pump and Dump Scheme").scale(1.5)

        self.play(Write(title))

        self.play(FadeOut(title))

        # Create a coordinate system
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            axis_config={"color": WHITE},
        )

        # Add labels to axes
        axes_labels = axes.get_axis_labels(x_label="t", y_label="\$")

        # Create a noisy "pump and dump" graph
        def noisy_pump_and_dump(x):
            # Pump (sharp rise around x=5)
            base = 5 + 90 * np.exp(-((x - 5) ** 2) / 2) if x < 5 else max(0, 100 - 70 * (x - 5))
            # Add random noise
            noise = 2 * np.sin(3 * x) + 2 * np.random.uniform(-1, 1)
            return max(0, base + noise)

        price_graph = axes.plot(
            noisy_pump_and_dump,
            x_range=[0, 9.5],
            color=RED,
            use_smoothing=True,
        )

        # Highlight key moments
        insider_pump_label = Text("Insiders Pump").next_to(axes.c2p(0.7, 30)).scale(0.5)
        others_pump_label = Text("Others Pump").next_to(axes.c2p(1.7, 70)).scale(0.5)
        dump_label = Text("Dump").next_to(axes.c2p(4.75, 90)).scale(0.5)

        # Play animations
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

        # --- Scraping Data ---

        self.next_slide()

        title = Text("Scraping").to_edge(UL)

        search_query = (
            Text("FTX Token site:reddit.com/r/CryptoCurrency after:2019-08-01 before:2022-11-07", color=GREY)
            .scale(0.5)
            .shift(UP * 1.5)
        )
        rectangle = SurroundingRectangle(search_query, color=GREY, buff=0.3)

        google_logo = ImageMobject("img/google_logo.png").scale(0.55).to_edge(LEFT).shift(DOWN * 0.7).shift(RIGHT * 0.5)
        reddit_logo = ImageMobject("img/reddit_logo.png").scale(0.55).shift(DOWN * 0.7)
        elastic_logo = (
            ImageMobject("img/elasticsearch_logo.png").scale(0.55).to_edge(RIGHT).shift(DOWN * 0.7).shift(LEFT * 0.5)
        )

        google_label = Text("Search for Reddit posts").next_to(google_logo, DOWN).scale(0.4)
        reddit_label = Text("Extracting data using praw").next_to(reddit_logo, DOWN).scale(0.4)
        elastic_label = Text("Store data in Elasticsearch").next_to(elastic_logo, DOWN).scale(0.4)

        arrow = Arrow(google_logo, reddit_logo).shift(DOWN * 1)
        arrow2 = Arrow(reddit_logo, elastic_logo).shift(DOWN * 1)

        self.play(Write(title, run_time=0.5))
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

        # --- Data Structure ---

        self.next_slide()

        title = Text("Data").to_edge(UL)

        reddit_structure = ImageMobject("img/reddit_structure.png").scale(0.8)
        reddit_structure.set_resampling_algorithm(RESAMPLING_ALGORITHMS["lanczos"])

        self.play(Write(title))
        self.play(FadeIn(reddit_structure))

        self.next_slide()

        self.play(FadeOut(title), FadeOut(reddit_structure))

        # --- Train and Test Split ---
        coin_image_size = 0.2
        coin_name_size = 0.3
        group_title_size = 0.4

        ts_title = Text("Train - Test Split").scale(0.9).to_edge(UL)
        self.play(Write(ts_title))

        train_non_scam_items = Group(
            *[
                Group(
                    ImageMobject("img/coin.png").scale(coin_image_size),
                    Text(name).scale(coin_name_size),
                ).arrange(DOWN, buff=0.1)
                for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain"]
            ]
        ).arrange(RIGHT, buff=0.5)

        train_scam_items = Group(
            *[
                Group(
                    ImageMobject("img/coin.png").scale(coin_image_size),
                    Text(name).scale(coin_name_size),
                ).arrange(DOWN, buff=0.1)
                for name in ["BeerCoin", "BitForex", "Terra Luna"]
            ]
        ).arrange(RIGHT, buff=0.5)

        test_non_scam_items = Group(
            *[
                Group(
                    ImageMobject("img/coin.png").scale(coin_image_size),
                    Text(name).scale(coin_name_size),
                ).arrange(DOWN, buff=0.1)
                for name in ["Cosmos", "Ethereum"]
            ]
        ).arrange(RIGHT, buff=0.5)

        test_scam_items = Group(
            *[
                Group(
                    ImageMobject("img/coin.png").scale(coin_image_size),
                    Text(name).scale(coin_name_size),
                ).arrange(DOWN, buff=0.1)
                for name in ["Safe Moon", "FTX Token"]
            ]
        ).arrange(RIGHT, buff=0.5)

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

        train_set_group = Group(train_non_scam_group, train_scam_group).arrange(DOWN, buff=1)
        test_set_group = Group(test_non_scam_group, test_scam_group).arrange(DOWN, buff=1)

        main_group = Group(train_set_group, test_set_group).arrange(RIGHT, buff=2)

        self.play(FadeIn(main_group))

        explanation_text = (
            Text("""
        Train set (7 coins): 4 Non-scam, 3 Scam
        Test set (4 coins): 2 Non-scam, 2 Scam
            """)
            .scale(0.5)
            .to_edge(DOWN)
        )
        self.play(Write(explanation_text))

        self.next_slide()

        self.play(
            FadeOut(ts_title),
            FadeOut(main_group),
            FadeOut(explanation_text),
        )

        # --- Training Methodology ---
        tm_title = Text("Training Methodology").scale(0.9).to_edge(UL)
        self.play(Write(tm_title))

        coin_image_size = 0.2
        coins = [
            Group(ImageMobject("img/coin.png").scale(coin_image_size), Text(name).scale(0.3)).arrange(DOWN, buff=0.1)
            for name in ["Avalanche", "Bitcoin", "Chainlink", "THORChain", "BeerCoin", "BitForex", "Terra Luna"]
        ]

        all_coins_group = Group(*coins).arrange(RIGHT, buff=0.5).shift(UP)

        validation_placeholder = Rectangle(
            width=all_coins_group.get_width(),
            height=all_coins_group.get_height(),
        ).set_opacity(0)

        fitting_group = Group(Text("Fitting Set").scale(0.5), all_coins_group).arrange(RIGHT, buff=0.8)

        validation_group = Group(Text("Validation Set").scale(0.5), validation_placeholder).arrange(RIGHT, buff=0.8)

        main_group = Group(fitting_group, validation_group).arrange(DOWN, buff=0.5)

        self.play(FadeIn(main_group))

        for coin in coins:
            self.play(coin.animate.shift(DOWN * 1.5))
            self.wait(0.5)
            self.play(coin.animate.shift(UP * 1.5))

        self.play(FadeOut(main_group), FadeOut(tm_title))

        # --- Multinomial Naive Bayes ---

        self.next_slide()

        mnb_title = Text("Multinomial Naive Bayes (Baseline)").scale(0.9).set_color(YELLOW).to_edge(UL)
        mnb_points = VGroup(
            Text("- Assumes independence between features").scale(0.5),
            Text("- Effective for text classification").scale(0.5),
            Text("- Requires numerical input").scale(0.5),
        ).arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(mnb_title))
        self.play(Write(mnb_points, shift=UP))

        self.next_slide()

        self.play(FadeOut(mnb_title, shift=DOWN), FadeOut(mnb_points, shift=DOWN))

        # --- Linear Support Vector Classifier ---

        self.next_slide()

        svc_title = Text("Linear Support Vector Classifier").scale(0.9).set_color(ORANGE).to_edge(UL)
        svc_points = VGroup(
            Text("- Maximizes margin between classes").scale(0.5),
            Text("- Requires numerical input").scale(0.5),
            Text("- Effective for linearly separable data").scale(0.5),
        ).arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(svc_title))
        self.play(Write(svc_points, shift=UP))

        self.next_slide()

        self.play(FadeOut(svc_title, shift=DOWN), FadeOut(svc_points, shift=DOWN))

        # --- Graph Attention Network ---

        self.next_slide()

        gat_title = Text("Graph Attention Network (GAT)").scale(0.9).set_color(GREEN).to_edge(UL)
        gat_graphic = ImageMobject("img/GAT.png").arrange(DOWN)

        self.play(Write(gat_title, run_time=0.5))
        self.play(FadeIn(gat_graphic, shift=UP))

        self.next_slide()

        self.play(FadeOut(gat_title, shift=DOWN), FadeOut(gat_graphic, shift=DOWN))
