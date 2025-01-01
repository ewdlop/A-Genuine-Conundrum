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
