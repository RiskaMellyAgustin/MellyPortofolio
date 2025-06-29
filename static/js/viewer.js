import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.module.js';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.160.1/examples/jsm/loaders/GLTFLoader.js';

const canvas = document.getElementById("three-canvas");

// ✅ Buat scene TANPA background hitam
const scene = new THREE.Scene();
// scene.background = new THREE.Color(0x000000); // ❌ Jangan pakai ini biar transparan

// ✅ Kamera
const camera = new THREE.PerspectiveCamera(
  45,
  window.innerWidth / window.innerHeight,
  0.1,
  100
);
camera.position.set(5, 5, 5);
camera.lookAt(0, 0, 0);

// ✅ Renderer dengan alpha = true (biar transparan)
const renderer = new THREE.WebGLRenderer({
  canvas,
  antialias: true,
  alpha: true, // ✅ ini penting
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);

// ✅ Lighting
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(2, 2, 2);
scene.add(light);

// ✅ Load GLB model
const loader = new GLTFLoader();
loader.load(
  '/static/models/desktop_pc/scene.gltf',
  (gltf) => {
    const model = gltf.scene;
    model.scale.set(1.5, 1.5, 1.5);
    scene.add(model);
    animate();
  },
  undefined,
  (error) => {
    console.error('❌ Failed to load model:', error);
  }
);

// ✅ Animasi
function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
