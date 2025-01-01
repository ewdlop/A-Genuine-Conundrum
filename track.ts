type Track = "main" | "alternative";
type Decision = "saveGroup" | "saveIndividual" | "indecision";

interface TrolleyProblem {
  trackStatus: {
    main: number; // Number of people on the main track
    alternative: number; // Number of people on the alternative track
  };
  decision: Decision;
  switchTrack: (track: Track) => void;
  getOutcome: () => string;
}


class Trolley implements TrolleyProblem {
  trackStatus = {
    main: 5, // Five people on the main track
    alternative: 1, // One person on the alternative track
  };

  decision: Decision = "indecision";

  switchTrack(track: Track): void {
    if (track === "main") {
      this.decision = "saveIndividual";
    } else if (track === "alternative") {
      this.decision = "saveGroup";
    } else {
      this.decision = "indecision";
    }
  }

  getOutcome(): string {
    switch (this.decision) {
      case "saveGroup":
        return "The trolley switches to the alternative track, saving the group but sacrificing one individual.";
      case "saveIndividual":
        return "The trolley remains on the main track, saving one individual but sacrificing the group.";
      case "indecision":
        return "The trolley proceeds on the main track, leading to the default outcome.";
      default:
        return "Undefined decision.";
    }
  }
}

// Example Usage
const trolley = new Trolley();
console.log(trolley.getOutcome()); // Initial state

trolley.switchTrack("alternative");
console.log(trolley.getOutcome()); // After decision
