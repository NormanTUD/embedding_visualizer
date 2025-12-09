#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

def generate_token_sequence(token_count):
    if not isinstance(token_count, int):
        raise TypeError("token_count must be an integer")
    if token_count <= 0:
        raise ValueError("token_count must be > 0")

    # Dynamische Clusterdefinition
    clusters = {
        "fruit_cluster": {
            "center": "fruit",
            "neighbors": ["apple", "banana"],
            "center_weight": 3,
            "neighbor_weight": 5
        },
        "animal_cluster": {
            "center": "animal",
            "neighbors": ["cat", "dog"],
            "center_weight": 3,
            "neighbor_weight": 5
        }
    }

    all_words = []
    for cluster_name in clusters:
        center = clusters[cluster_name]["center"]
        neighbors = clusters[cluster_name]["neighbors"]
        # Zentrum: moderate Wahrscheinlichkeit
        for _ in range(clusters[cluster_name]["center_weight"]):
            all_words.append(center)
        # Nachbarn: höhere Wahrscheinlichkeit
        for _ in range(clusters[cluster_name]["neighbor_weight"]):
            for n in neighbors:
                all_words.append(n)

    if len(all_words) == 0:
        raise RuntimeError("No words available for sampling")

    result_tokens = []

    for _ in range(token_count):
        w = random.choice(all_words)
        result_tokens.append(w)
        
        # Mit kleiner Wahrscheinlichkeit Nachbarschaftsverstärkung
        if random.random() < 0.35:
            for cluster_name in clusters:
                center = clusters[cluster_name]["center"]
                neighbors = clusters[cluster_name]["neighbors"]
                if w == center:
                    result_tokens.append(random.choice(neighbors))
                elif w in neighbors:
                    result_tokens.append(center)

    return " ".join(result_tokens)


def main():
    if len(sys.argv) != 2:
        print("Usage: python generate.py <token_count>")
        sys.exit(1)

    try:
        token_count = int(sys.argv[1])
    except Exception as e:
        print("Error: token_count must be an integer")
        print(e)
        sys.exit(1)

    try:
        output = generate_token_sequence(token_count)
    except Exception as e:
        print("Generation error:", e)
        sys.exit(1)

    print(output)


if __name__ == "__main__":
    main()
