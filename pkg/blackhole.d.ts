/* tslint:disable */
/* eslint-disable */

/**
 * Rendering for the blackhole and rays.
 * and also managment of objects in the scene
 */
export class Renderer {
    free(): void;
    [Symbol.dispose](): void;
    add_ray_from_click(mouse_x: number, mouse_y: number): void;
    buffer_ptr(): number;
    constructor();
    set_blackhole_mass(mass: number): void;
    update(): void;
}

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
    readonly memory: WebAssembly.Memory;
    readonly __wbg_renderer_free: (a: number, b: number) => void;
    readonly renderer_add_ray_from_click: (a: number, b: number, c: number) => [number, number];
    readonly renderer_buffer_ptr: (a: number) => number;
    readonly renderer_new: () => number;
    readonly renderer_set_blackhole_mass: (a: number, b: number) => [number, number];
    readonly renderer_update: (a: number) => void;
    readonly __wbindgen_externrefs: WebAssembly.Table;
    readonly __externref_table_dealloc: (a: number) => void;
    readonly __wbindgen_start: () => void;
}

export type SyncInitInput = BufferSource | WebAssembly.Module;

/**
 * Instantiates the given `module`, which can either be bytes or
 * a precompiled `WebAssembly.Module`.
 *
 * @param {{ module: SyncInitInput }} module - Passing `SyncInitInput` directly is deprecated.
 *
 * @returns {InitOutput}
 */
export function initSync(module: { module: SyncInitInput } | SyncInitInput): InitOutput;

/**
 * If `module_or_path` is {RequestInfo} or {URL}, makes a request and
 * for everything else, calls `WebAssembly.instantiate` directly.
 *
 * @param {{ module_or_path: InitInput | Promise<InitInput> }} module_or_path - Passing `InitInput` directly is deprecated.
 *
 * @returns {Promise<InitOutput>}
 */
export default function __wbg_init (module_or_path?: { module_or_path: InitInput | Promise<InitInput> } | InitInput | Promise<InitInput>): Promise<InitOutput>;
