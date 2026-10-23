// Marigold Twilight Theme — plum dusk and marigold light
import { readFile } from 'node:fs/promises';

const DUSK_PALETTE = {
  night: '#522D60',
  plum: '#80426E',
  marigold: '#F2A67B',
  amber: '#FFD38B',
};

export class TwilightGarden {
  constructor(name = 'Evening border') {
    this.name = name;
    this.palette = DUSK_PALETTE;
  }

  /** Blend dusk into light and return the hex shade. */
  blend(from, to, ratio = 0.5) {
    const parse = (hex) =>
      [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channel = (value, i) =>
      Math.round(value * (1 - ratio) + b[i] * ratio);
    const toHex = (value) => value.toString(16).padStart(2, '0');
    return '#' + a.map(channel).map(toHex).join('');
  }

  async readPlan(file) {
    const content = await readFile(file, 'utf8');
    const rows = content.split('\n').filter(Boolean);
    return {
      name: this.name,
      shades: Object.keys(this.palette).length,
      rows: rows.length,
      content,
    };
  }
}

const garden = new TwilightGarden();
const glow = garden.blend(DUSK_PALETTE.night, DUSK_PALETTE.amber);

console.log(`dusk glow: ${glow}`);
